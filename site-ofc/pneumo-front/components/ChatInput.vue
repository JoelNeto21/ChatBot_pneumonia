<template>
  <div class="px-4 md:px-8 pb-6 pt-2 relative z-20 w-full max-w-4xl mx-auto">
    
    <div class="absolute right-6 md:right-10 top-0 transform -translate-y-full mb-2 flex items-center gap-4">
      <span v-if="imagePreviews.length > 0" :class="['text-[11px] font-bold transition-colors', imagePreviews.length >= MAX_IMAGES ? 'text-rose-500' : 'text-blue-500']">
        <i class="fas fa-image mr-1"></i> {{ imagePreviews.length }}/{{ MAX_IMAGES }}
      </span>
      <span :class="['text-[11px] font-bold transition-colors', isNearLimit ? 'text-amber-500' : 'text-slate-400 dark:text-slate-500']">
        {{ messageText.length }}/{{ MAX_CHARS }}
      </span>
    </div>

    <div 
      @dragover.prevent="isDragging = true" 
      @dragleave.prevent="isDragging = false" 
      @drop.prevent="handleDrop"
      :class="[
        'bg-slate-100 dark:bg-[#1f2228] transition-all flex flex-col relative',
        // Se tiver imagens anexadas ou texto longo, fica arredondado tipo card, senão fica uma pílula perfeita
        (imagePreviews.length > 0 || messageText.length > 50) ? 'rounded-3xl p-2' : 'rounded-[32px] p-1.5',
        isDragging ? 'ring-2 ring-indigo-500 bg-indigo-50 dark:bg-indigo-900/20 scale-[1.01]' : 'focus-within:ring-1 focus-within:ring-slate-300 dark:focus-within:ring-white/20 shadow-sm'
      ]"
    >
      
      <div v-if="isDragging" class="absolute inset-0 z-50 flex items-center justify-center bg-white/90 dark:bg-[#1f2228]/90 backdrop-blur-sm rounded-[inherit] border-2 border-dashed border-indigo-500">
        <div class="text-indigo-500 font-bold flex items-center gap-2 animate-bounce text-sm">
          <i class="fas fa-cloud-upload-alt text-lg"></i> Solte os exames
        </div>
      </div>

      <div v-if="imagePreviews.length > 0" class="px-3 pt-3 pb-1 flex gap-3 overflow-x-auto no-scrollbar">
        <div v-for="(img, idx) in imagePreviews" :key="idx" class="relative inline-block animate-in zoom-in duration-200 flex-shrink-0 group">
          <img :src="img" class="h-14 w-14 md:h-16 md:w-16 object-cover rounded-2xl border border-slate-200 dark:border-white/10 shadow-sm" alt="Preview" />
          <button @click="removeImage(idx)" aria-label="Remover" class="absolute -top-2 -right-2 bg-slate-800 dark:bg-slate-700 text-white rounded-full w-5 h-5 flex items-center justify-center text-[9px] hover:bg-rose-500 transition-all shadow-md transform scale-90 group-hover:scale-100">
            <i class="fas fa-times"></i>
          </button>
        </div>
      </div>

      <div class="flex items-end gap-1">
        <input type="file" ref="fileInputRef" @change="handleFileChange" accept="image/png, image/jpeg, image/jpg" multiple class="hidden" />
        
        <button 
          @click="triggerFileInput" 
          :disabled="imagePreviews.length >= MAX_IMAGES"
          class="p-3 w-10 h-10 flex items-center justify-center text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white transition-colors rounded-full focus:outline-none disabled:opacity-40 disabled:cursor-not-allowed mb-0.5 ml-0.5" 
          title="Anexar Exames"
        >
          <i class="fas fa-plus text-[16px]"></i>
        </button>

        <textarea 
          ref="textareaRef" 
          v-model="messageText" 
          @keydown.enter="handleEnter" 
          @paste="handlePaste" 
          @input="adjustHeight"
          :maxlength="MAX_CHARS"
          :placeholder="inputPlaceholder"
          class="flex-1 max-h-32 min-h-[44px] bg-transparent border-none focus:ring-0 resize-none py-2.5 px-2 text-[15.5px] font-medium text-slate-800 dark:text-slate-100 placeholder-slate-400 dark:placeholder-slate-500 no-scrollbar outline-none leading-relaxed"
          rows="1" 
          :disabled="isRecording"
        ></textarea>

        <button 
          @click="toggleRecording" 
          :class="['p-3 w-10 h-10 flex items-center justify-center transition-all rounded-full focus:outline-none mb-0.5', isRecording ? 'text-rose-500 bg-rose-50 dark:bg-rose-500/10' : 'text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white']" 
          title="Gravar por Voz"
        >
          <i :class="['fas text-[16px]', isRecording ? 'fa-microphone animate-pulse' : 'fa-microphone-alt']"></i>
        </button>

        <button 
          @click="handleMainAction" 
          :disabled="isSendDisabled && !isGenerating" 
          :class="[
            'w-10 h-10 rounded-full flex items-center justify-center transition-all focus:outline-none mb-0.5 mr-0.5',
            isGenerating ? 'bg-slate-800 dark:bg-white text-white dark:text-slate-900 hover:scale-105 shadow-md' : 
            (isSendDisabled ? 'bg-slate-200 dark:bg-white/5 text-slate-400 dark:text-slate-600' : 'bg-slate-800 dark:bg-white text-white dark:text-slate-900 hover:scale-105 shadow-md')
          ]"
        >
          <i v-if="isGenerating" class="fas fa-square text-[12px]"></i>
          <i v-else class="fas fa-arrow-up text-[16px]"></i>
        </button>
      </div>
    </div>
    
    <div class="text-center mt-3">
      <p class="text-[11px] text-slate-400/70 font-medium tracking-wide">
        A IA assiste, mas não substitui a avaliação médica.
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, nextTick, onMounted } from 'vue';

// Adicionada a prop "isGenerating" para sabermos quando a IA está a escrever
const props = defineProps<{ isGenerating?: boolean }>();

const emit = defineEmits<{ 
  (e: 'sendMessage', payload: { text: string; images: string[] }): void;
  (e: 'stopGeneration'): void; // Novo evento para parar a IA
}>();

const MAX_CHARS = 2000;
const MAX_IMAGES = 4;

const messageText = ref('');
const textareaRef = ref<HTMLTextAreaElement | null>(null);
const fileInputRef = ref<HTMLInputElement | null>(null);
const imagePreviews = ref<string[]>([]);
const isDragging = ref(false);
const isRecording = ref(false);

let recognition: any = null;

const isNearLimit = computed(() => messageText.value.length >= MAX_CHARS * 0.9);

const inputPlaceholder = computed(() => {
  if (isRecording.value) return 'A ouvir a sua voz...';
  if (imagePreviews.value.length >= MAX_IMAGES) return 'Limite atingido. Descreva os sintomas...';
  return 'Pergunte ao PneumoAssist...';
});

const isSendDisabled = computed(() => {
  return (!messageText.value.trim() && imagePreviews.value.length === 0) || isRecording.value;
});

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
        else {
           const preview = event.results[i][0].transcript;
           if ((messageText.value + preview).length <= MAX_CHARS) {
              messageText.value = preview; 
           }
        }
      }
      if (finalTranscript) {
        const currentText = messageText.value.trim();
        const newText = currentText ? `${currentText} ${finalTranscript}` : finalTranscript;
        messageText.value = newText.substring(0, MAX_CHARS);
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

const triggerFileInput = () => {
  if (imagePreviews.value.length >= MAX_IMAGES) return;
  fileInputRef.value?.click();
};

const processFile = (file: File) => {
  if (!file.type.startsWith('image/')) return;
  if (imagePreviews.value.length >= MAX_IMAGES) return;

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

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files?.length) {
    const filesArray = Array.from(target.files);
    const slotsAvailable = MAX_IMAGES - imagePreviews.value.length;
    filesArray.slice(0, slotsAvailable).forEach(processFile);
    target.value = ''; 
  }
};

const handlePaste = (e: ClipboardEvent) => {
  if (e.clipboardData?.items) {
    let slotsAvailable = MAX_IMAGES - imagePreviews.value.length;
    for (const item of e.clipboardData.items) {
      if (slotsAvailable <= 0) break;
      if (item.type.startsWith('image/')) {
        const file = item.getAsFile();
        if (file) {
          processFile(file);
          slotsAvailable--;
        }
      }
    }
  }
};

const handleDrop = (e: DragEvent) => {
  isDragging.value = false;
  if (e.dataTransfer?.files) {
    const filesArray = Array.from(e.dataTransfer.files);
    const slotsAvailable = MAX_IMAGES - imagePreviews.value.length;
    filesArray.slice(0, slotsAvailable).forEach(processFile);
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

// Nova Função Dinâmica: Envia a mensagem OU para a geração da IA
const handleMainAction = () => {
  if (props.isGenerating) {
    emit('stopGeneration');
  } else if (!isSendDisabled.value) {
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
    if (!props.isGenerating) handleMainAction(); 
  }
};
</script>

<style scoped>
/* Remove visualmente a barra de rolagem mas mantém o scroll funcional */
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none; 
  scrollbar-width: none; 
}
</style>