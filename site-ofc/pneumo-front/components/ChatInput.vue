<template>
  <div class="w-full flex-shrink-0 bg-white/90 dark:bg-slate-950/90 backdrop-blur-xl border-t border-slate-200/60 dark:border-slate-800/60 px-4 md:px-8 py-5 relative z-20">
    <div class="max-w-4xl mx-auto">
      
      <div 
        @dragover.prevent="isDragging = true" 
        @dragleave.prevent="isDragging = false" 
        @drop.prevent="handleDrop"
        :class="[
          'bg-white dark:bg-slate-900 border-2 rounded-2xl p-2 shadow-sm transition-all flex flex-col relative',
          isDragging ? 'border-indigo-500 bg-indigo-50/50 dark:bg-indigo-900/20' : 'border-slate-200 dark:border-slate-800 focus-within:ring-2 focus-within:ring-indigo-500/30 focus-within:border-indigo-500/50'
        ]"
      >
        
        <div v-if="isDragging" class="absolute inset-0 z-50 flex items-center justify-center bg-white/80 dark:bg-slate-900/80 backdrop-blur-sm rounded-2xl border-2 border-dashed border-indigo-500">
          <p class="text-indigo-600 dark:text-indigo-400 font-bold flex items-center gap-2">
            <i class="fas fa-cloud-upload-alt text-xl"></i> Largar imagem aqui
          </p>
        </div>

        <div v-if="imagePreviews.length > 0" class="px-3 pt-3 pb-2 flex gap-3 overflow-x-auto custom-scrollbar">
          <div v-for="(img, idx) in imagePreviews" :key="idx" class="relative inline-block animate-in zoom-in duration-200 flex-shrink-0 group">
            <img :src="img" class="h-20 w-20 object-cover rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm" alt="Preview do exame" />
            <button @click="removeImage(idx)" aria-label="Remover imagem" class="absolute -top-2 -right-2 bg-slate-800 dark:bg-slate-700 text-white rounded-full w-6 h-6 flex items-center justify-center text-[10px] hover:bg-rose-500 transition-all opacity-0 group-hover:opacity-100 shadow-md transform scale-90 group-hover:scale-100">
              <i class="fas fa-times"></i>
            </button>
          </div>
        </div>

        <div class="flex items-end gap-2">
          <input type="file" ref="fileInputRef" @change="handleFileChange" accept="image/png, image/jpeg, image/jpg" multiple class="hidden" />
          <button @click="triggerFileInput" aria-label="Anexar ficheiros" class="p-3 text-slate-400 hover:text-indigo-600 transition-colors rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500/50" title="Anexar Exames">
            <i class="fas fa-paperclip text-[17px]"></i>
          </button>

          <button @click="toggleRecording" aria-label="Gravar voz" :class="['p-3 transition-all rounded-xl relative overflow-hidden group focus:outline-none', isRecording ? 'text-rose-500 hover:bg-rose-50 dark:hover:bg-rose-900/20' : 'text-slate-400 hover:text-indigo-600 hover:bg-slate-100 dark:hover:bg-slate-800']" title="Gravar Sintomas por Voz">
            <div v-if="isRecording" class="absolute inset-0 bg-rose-500/20 animate-ping rounded-xl"></div>
            <i :class="['fas text-[17px] relative z-10', isRecording ? 'fa-microphone animate-pulse' : 'fa-microphone-alt']"></i>
          </button>

          <textarea 
            ref="textareaRef" 
            v-model="messageText" 
            @keydown.enter="handleEnter" 
            @paste="handlePaste" 
            @input="adjustHeight"
            :placeholder="isRecording ? 'A ouvir a sua voz...' : 'Descreva os sintomas ou arraste exames para aqui...'"
            class="flex-1 max-h-32 min-h-[44px] bg-transparent border-none focus:ring-0 resize-none py-3 px-2 text-[15px] font-medium text-slate-800 dark:text-slate-100 placeholder-slate-400 dark:placeholder-slate-500 custom-scrollbar outline-none"
            rows="1" 
            :disabled="isRecording"
          ></textarea>

          <button @click="send" aria-label="Enviar mensagem" :disabled="isSendDisabled" class="w-11 h-11 rounded-xl bg-gradient-to-br from-indigo-500 to-indigo-600 hover:from-indigo-600 hover:to-indigo-700 text-white flex items-center justify-center transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-md shadow-indigo-500/20 mb-0.5 mr-0.5 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 dark:focus:ring-offset-slate-900">
            <i class="fas fa-paper-plane text-[15px] translate-y-[1px] -translate-x-[1px]"></i>
          </button>
        </div>
      </div>
      
      <div class="text-center mt-3">
        <p class="text-[11px] text-slate-400 font-medium tracking-wide">Os dados processados pela IA não substituem o diagnóstico de um médico.</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, nextTick, onMounted } from 'vue';

const emit = defineEmits<{ (e: 'sendMessage', payload: { text: string; images: string[] }): void }>();

const messageText = ref('');
const textareaRef = ref<HTMLTextAreaElement | null>(null);
const fileInputRef = ref<HTMLInputElement | null>(null);
const imagePreviews = ref<string[]>([]);
const isDragging = ref(false);
const isRecording = ref(false);

let recognition: any = null;

// Otimização: Computed para gerir o estado desativado do botão de envio
const isSendDisabled = computed(() => {
  return (!messageText.value.trim() && imagePreviews.value.length === 0) || isRecording.value;
});

// Inicialização da API de Voz
onMounted(() => {
  const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
  if (SpeechRecognition) {
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = true;
    recognition.lang = 'pt-PT';
    
    recognition.onresult = (event: any) => {
      let finalTranscript = '';
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) finalTranscript += event.results[i][0].transcript;
        else messageText.value = event.results[i][0].transcript; 
      }
      if (finalTranscript) {
        const currentText = messageText.value.trim();
        messageText.value = currentText ? `${currentText} ${finalTranscript}` : finalTranscript;
        adjustHeight();
      }
    };
    recognition.onerror = () => { isRecording.value = false; };
    recognition.onend = () => { 
      isRecording.value = false; 
      nextTick(() => textareaRef.value?.focus()); 
    };
  }
});

const toggleRecording = () => {
  if (!recognition) return alert("O seu navegador não suporta a gravação de voz.");
  if (isRecording.value) recognition.stop();
  else { recognition.start(); isRecording.value = true; }
};

const triggerFileInput = () => fileInputRef.value?.click();

// Otimização: Função de processamento de ficheiros mais limpa
const processFile = (file: File) => {
  if (!file.type.startsWith('image/')) return; // Proteção contra ficheiros não-imagem

  const reader = new FileReader();
  reader.onload = (e) => {
    const img = new Image();
    img.onload = () => {
      const canvas = document.createElement('canvas');
      const MAX_SIZE = 800;
      let { width, height } = img;

      if (width > height && width > MAX_SIZE) {
        height *= MAX_SIZE / width;
        width = MAX_SIZE;
      } else if (height > MAX_SIZE) {
        width *= MAX_SIZE / height;
        height = MAX_SIZE;
      }

      canvas.width = width;
      canvas.height = height;
      const ctx = canvas.getContext('2d');
      ctx?.drawImage(img, 0, 0, width, height);
      imagePreviews.value.push(canvas.toDataURL('image/jpeg', 0.8));
    };
    img.src = e.target?.result as string;
  };
  reader.readAsDataURL(file);
};

// Eventos de Ficheiro (Input, Paste, Drop)
const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files?.length) {
    Array.from(target.files).forEach(processFile);
    target.value = ''; 
  }
};

const handlePaste = (e: ClipboardEvent) => {
  if (e.clipboardData?.items) {
    for (const item of e.clipboardData.items) {
      if (item.type.startsWith('image/')) {
        const file = item.getAsFile();
        if (file) processFile(file);
      }
    }
  }
};

const handleDrop = (e: DragEvent) => {
  isDragging.value = false;
  if (e.dataTransfer?.files) {
    Array.from(e.dataTransfer.files).forEach(processFile);
  }
};

const removeImage = (index: number) => { 
  imagePreviews.value.splice(index, 1); 
};

const adjustHeight = () => {
  nextTick(() => {
    const el = textareaRef.value;
    if (el) { 
      el.style.height = 'auto'; 
      el.style.height = `${el.scrollHeight}px`; 
    }
  });
};

const send = () => {
  if (!isSendDisabled.value) {
    emit('sendMessage', { text: messageText.value, images: [...imagePreviews.value] });
    messageText.value = '';
    imagePreviews.value = [];
    nextTick(() => { 
      if (textareaRef.value) textareaRef.value.style.height = 'auto'; 
    });
  }
};

const handleEnter = (e: KeyboardEvent) => {
  if (!e.shiftKey && !isRecording.value) { 
    e.preventDefault(); 
    send(); 
  }
};
</script>