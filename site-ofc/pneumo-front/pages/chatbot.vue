<template>
  <div class="flex h-screen w-full overflow-hidden bg-[#f8fafc] dark:bg-slate-950 relative text-slate-800 dark:text-slate-200" style="font-family: 'Open Sans', sans-serif;">
    
    <Sidebar :is-open="isSidebarOpen" @toggle="isSidebarOpen = !isSidebarOpen" />

    <div class="absolute top-5 left-5 right-5 flex justify-between z-30 pointer-events-none">
      <button v-if="!isSidebarOpen" @click="isSidebarOpen = true" class="w-11 h-11 bg-white/80 dark:bg-slate-900/80 border border-slate-200/50 dark:border-slate-800/50 backdrop-blur-md text-slate-500 dark:text-slate-400 rounded-2xl flex items-center justify-center shadow-sm hover:shadow hover:text-indigo-600 transition-all pointer-events-auto group" aria-label="Abrir menu">
        <i class="fas fa-bars group-hover:scale-110 transition-transform"></i>
      </button>
      <div v-else></div>

      <button @click="isTopicsOpen = !isTopicsOpen" :class="['w-11 h-11 bg-white/80 dark:bg-slate-900/80 border border-slate-200/50 dark:border-slate-800/50 backdrop-blur-md text-slate-500 dark:text-slate-400 rounded-2xl flex items-center justify-center shadow-sm hover:shadow transition-all pointer-events-auto group', isTopicsOpen ? 'text-indigo-600 dark:text-indigo-400' : 'hover:text-indigo-600']" :title="isTopicsOpen ? 'Ocultar Tópicos' : 'Mostrar Tópicos'">
        <i :class="isTopicsOpen ? 'fas fa-chevron-right' : 'fas fa-history group-hover:scale-110 transition-transform'"></i>
      </button>
    </div>

    <main class="flex-1 flex flex-col relative overflow-hidden">
      <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] bg-opacity-[0.15] dark:opacity-5 pointer-events-none"></div>

      <div class="flex-1 flex overflow-hidden z-10">
        
        <div class="flex-1 flex flex-col relative overflow-hidden">
          
          <div ref="scrollContainer" @scroll="handleScroll" class="flex-1 overflow-y-auto px-4 md:px-8 lg:px-12 py-8 pt-24 custom-scrollbar scroll-smooth">
            <div class="max-w-3xl mx-auto space-y-12 pb-36">
              
              <div v-if="messages.length <= 1" class="flex flex-col items-center py-16 text-center animate-in fade-in zoom-in duration-700">
                <div class="relative mb-8">
                  <div class="absolute inset-0 bg-indigo-500/20 blur-2xl rounded-full"></div>
                  <KoalaIcon expression="happy" class="scale-125 relative z-10 drop-shadow-xl" />
                </div>
                <h3 class="text-slate-800 dark:text-white font-extrabold text-3xl md:text-4xl mb-4 tracking-tight" style="font-family: 'Montserrat', sans-serif;">Como posso ajudar hoje?</h3>
                <p class="text-slate-500 dark:text-slate-400 max-w-md mx-auto text-[15px] leading-relaxed">Descreva os sintomas, anexe exames de imagem ou fale diretamente ao microfone para começarmos a análise clínica.</p>
              </div>

              <div v-for="(msg, index) in messages" :key="index" :id="'msg-' + index" class="w-full relative">
                
                <div v-if="msg.sender === 'bot'" class="flex gap-4 md:gap-5 w-full animate-in slide-in-from-left-4 duration-300">
                  <KoalaIcon :expression="msg.expression || 'neutral'" class="mt-1 shadow-sm" />
                  
                  <div class="flex-1 overflow-hidden min-w-0 pt-1">
                    <div class="flex items-center gap-2 mb-1.5">
                      <span class="font-extrabold text-[13px] text-slate-800 dark:text-slate-200" style="font-family: 'Montserrat', sans-serif;">PneumoAssist IA</span>
                      <i class="fas fa-badge-check text-indigo-500 text-[11px]"></i>
                    </div>
                    
                    <div class="text-slate-700 dark:text-slate-300 leading-relaxed text-[15px]">
                      <div class="markdown-body" v-html="renderMarkdown(msg.text)"></div>
                      
                      <div v-if="msg.isTyping" class="mt-3 flex items-center gap-2 text-indigo-500 text-sm font-semibold opacity-80 animate-pulse">
                        <i class="fas fa-circle-notch fa-spin text-xs"></i> A redigir relatório...
                      </div>

                      <div v-if="msg.isPaused" class="mt-4 flex items-center gap-3 animate-in fade-in zoom-in bg-amber-50 dark:bg-amber-900/10 border border-amber-200 dark:border-amber-800/30 p-3 rounded-2xl w-fit">
                        <span class="text-xs text-amber-600 dark:text-amber-500 font-bold flex items-center gap-1.5">
                          <i class="fas fa-pause-circle"></i> Análise em pausa
                        </span>
                        <button @click="resumeGeneration(index)" class="px-4 py-1.5 bg-amber-500 hover:bg-amber-600 text-white rounded-xl text-xs font-bold transition-colors shadow-sm">
                          Continuar
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <div v-else class="flex justify-end group relative w-full">
                  <div class="max-w-[85%] md:max-w-[70%] flex flex-col items-end relative">
                    
                    <div class="absolute -left-12 top-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 hidden md:flex z-10">
                      <button @click="startEdit(index)" class="w-8 h-8 bg-white dark:bg-slate-800 rounded-full shadow-sm border border-slate-200 dark:border-slate-700 text-slate-400 hover:text-indigo-500 hover:bg-slate-50 transition-all flex items-center justify-center" title="Editar Mensagem">
                        <i class="fas fa-pen text-xs"></i>
                      </button>
                    </div>

                    <div v-if="msg.isEditing" class="w-full min-w-[280px] md:min-w-[400px] bg-white dark:bg-slate-900 p-4 rounded-3xl rounded-tr-sm border-2 border-indigo-500 shadow-xl animate-in zoom-in-95 duration-200">
                      <div class="flex items-center gap-2 mb-3 text-[11px] font-extrabold text-indigo-500 uppercase tracking-widest" style="font-family: 'Montserrat', sans-serif;">
                        <i class="fas fa-edit"></i> Edição de Sintomas
                      </div>
                      
                      <div v-if="msg.editImages && msg.editImages.length > 0" class="flex gap-2 mb-3 overflow-x-auto custom-scrollbar pb-1">
                        <div v-for="(img, imgIdx) in msg.editImages" :key="imgIdx" class="relative group/img flex-shrink-0">
                          <img :src="img" class="h-16 w-16 object-cover rounded-xl border border-slate-200 dark:border-slate-700" />
                          <button @click="msg.editImages?.splice(imgIdx, 1)" class="absolute -top-1.5 -right-1.5 bg-slate-800 text-white rounded-full w-5 h-5 flex items-center justify-center text-[9px] hover:bg-rose-500 transition-colors shadow-sm opacity-0 group-hover/img:opacity-100">
                            <i class="fas fa-times"></i>
                          </button>
                        </div>
                      </div>

                      <textarea 
                        v-model="msg.editText" 
                        @paste="handleEditPaste($event, index)"
                        placeholder="Edite o texto ou cole novas imagens aqui (Ctrl+V)..."
                        class="w-full bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 text-slate-800 dark:text-slate-200 resize-none custom-scrollbar text-[15px] leading-relaxed transition-all" 
                        rows="3"
                      ></textarea>
                      <div class="flex justify-end gap-2 mt-3">
                        <button @click="cancelEdit(index)" class="px-4 py-2 rounded-xl text-xs font-bold text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">Cancelar</button>
                        <button @click="submitEdit(index)" class="px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 text-white hover:bg-indigo-700 transition-colors shadow-sm shadow-indigo-500/30">Atualizar</button>
                      </div>
                    </div>

                    <div v-else class="bg-indigo-600 dark:bg-indigo-600 text-white rounded-3xl rounded-tr-md px-5 py-3.5 shadow-sm hover:shadow-md transition-shadow cursor-pointer break-words w-full" @dblclick="startEdit(index)">
                      
                      <div v-if="msg.images && msg.images.length > 0" class="w-full max-w-[340px] mb-3">
                        <div :class="['grid gap-2', msg.images.length === 1 ? 'grid-cols-1' : 'grid-cols-2']">
                          <div v-for="(img, imgIdx) in msg.images" :key="imgIdx" class="relative aspect-square">
                            <img :src="img" class="w-full h-full object-cover rounded-2xl border border-white/10 shadow-sm" alt="Exame Clínico anexado" />
                          </div>
                        </div>
                      </div>

                      <p v-if="msg.text" class="text-[15px] leading-relaxed whitespace-pre-wrap">{{ msg.text }}</p>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>

          <button v-show="isUserScrolledUp" @click="forceScrollToBottom" class="absolute bottom-28 left-1/2 -translate-x-1/2 md:left-auto md:translate-x-0 md:right-8 w-10 h-10 bg-white/90 dark:bg-slate-800/90 backdrop-blur-md text-indigo-500 rounded-full shadow-lg border border-slate-200 dark:border-slate-700 flex items-center justify-center hover:scale-110 hover:bg-indigo-50 dark:hover:bg-slate-700 hover:text-indigo-600 transition-all z-40 animate-bounce" title="Ir para o fim">
            <i class="fas fa-arrow-down text-sm"></i>
          </button>

          <div v-if="isGenerating" class="absolute bottom-24 left-1/2 -translate-x-1/2 z-40">
            <button @click="stopGeneration" class="px-5 py-2.5 bg-slate-900/90 dark:bg-white/90 backdrop-blur-md text-white dark:text-slate-900 rounded-full shadow-lg font-bold text-[11px] uppercase tracking-widest flex items-center gap-2 hover:scale-105 transition-all animate-in slide-in-from-bottom-4 border border-slate-700 dark:border-slate-200">
              <i class="fas fa-stop-circle text-rose-500"></i> Pausar Relatório
            </button>
          </div>

          <div class="relative z-30">
            <ChatInput @sendMessage="handleSendMessage" />
          </div>
        </div>

        <aside :class="['transition-all duration-300 ease-in-out flex flex-col bg-slate-50/80 dark:bg-slate-900/50 backdrop-blur-xl border-l border-slate-200/60 dark:border-slate-800/60 z-20 overflow-hidden flex-shrink-0', isTopicsOpen ? 'w-72 md:w-80 opacity-100 translate-x-0' : 'w-0 opacity-0 translate-x-full border-transparent']">
          <div class="px-6 py-5 border-b border-slate-200/60 dark:border-slate-800/60 flex-shrink-0">
            <h3 class="font-extrabold text-slate-800 dark:text-slate-200 flex items-center gap-2 text-xs uppercase tracking-widest" style="font-family: 'Montserrat', sans-serif;">
              <i class="fas fa-history text-indigo-500"></i> Histórico da Sessão
            </h3>
          </div>
          <div class="flex-1 overflow-y-auto custom-scrollbar p-3 space-y-1.5">
            <div v-if="chatTopics.length === 0" class="text-center text-slate-400 dark:text-slate-500 text-[11px] mt-12 px-4">
              <div class="w-12 h-12 rounded-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center mx-auto mb-3 text-slate-300 dark:text-slate-600">
                <i class="fas fa-scroll text-lg"></i>
              </div>
              <p>O índice será criado automaticamente à medida que fizer perguntas.</p>
            </div>
            
            <button v-for="topic in chatTopics" :key="topic.originalIndex" @click="scrollToMessage(topic.originalIndex)" class="w-full text-left p-3.5 rounded-2xl hover:bg-white dark:hover:bg-slate-800 hover:shadow-sm border border-transparent hover:border-slate-200 dark:hover:border-slate-700 transition-all group">
              <div class="flex items-start gap-3">
                <div class="mt-0.5 text-slate-300 dark:text-slate-600 group-hover:text-indigo-500 transition-colors">
                  <i :class="topic.images?.length ? 'fas fa-image' : 'fas fa-comment-dots'"></i>
                </div>
                <p class="text-[13px] font-semibold text-slate-600 dark:text-slate-300 group-hover:text-slate-900 dark:group-hover:text-white line-clamp-2 leading-snug">
                  {{ topic.text || 'Análise de Exame de Imagem' }}
                </p>
              </div>
            </button>
          </div>
        </aside>

      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, nextTick, onMounted } from 'vue';
import { marked } from 'marked';
import Sidebar from '~/components/Sidebar.vue';
import ChatInput from '~/components/ChatInput.vue';
import KoalaIcon from '~/components/KoalaIcon.vue'; 

const isSidebarOpen = ref(false);
const isTopicsOpen = ref(true);
const scrollContainer = ref<HTMLElement | null>(null);
const isGenerating = ref(false);
const isUserScrolledUp = ref(false);

interface Message {
  sender: 'user' | 'bot';
  text: string;
  expression?: 'neutral' | 'happy' | 'analytical' | 'worried' | 'sad' | 'serious' | 'wink' | 'confused' | 'surprised'; 
  images?: string[]; // MULTIPLAS IMAGENS
  isTyping?: boolean;
  isPaused?: boolean;
  isEditing?: boolean;
  editText?: string;
  editImages?: string[]; // IMAGENS COLADAS NA EDIÇÃO
}

const messages = ref<Message[]>([
  { sender: 'bot', text: 'Olá! 👋 Sou o **PneumoAssist**, a sua IA Clínica. 🫁\n\nEstou pronto para analisar casos, esclarecer dúvidas pneumológicas ou interpretar exames. Como posso ajudar hoje? ✨', expression: 'happy' }
]);

const renderMarkdown = (text: string) => {
  return marked(text, { breaks: true, gfm: true }) as string;
};

const handleScroll = () => {
  if (!scrollContainer.value) return;
  const { scrollTop, scrollHeight, clientHeight } = scrollContainer.value;
  isUserScrolledUp.value = scrollHeight - scrollTop - clientHeight > 100;
};

const scrollToBottom = () => {
  if (isUserScrolledUp.value) return; 
  nextTick(() => {
    if (scrollContainer.value) scrollContainer.value.scrollTop = scrollContainer.value.scrollHeight;
  });
};

const forceScrollToBottom = () => {
  isUserScrolledUp.value = false;
  nextTick(() => {
    if (scrollContainer.value) scrollContainer.value.scrollTo({ top: scrollContainer.value.scrollHeight, behavior: 'smooth' });
  });
};

let typewriterTimer: any = null;
const typeState = ref({ active: false, paused: false, text: '', index: 0, msgIndex: -1 });

const typeWriter = (messageIndex: number, fullText: string, resume = false) => {
  isGenerating.value = true;
  const newMessage = messages.value[messageIndex];
  newMessage.isTyping = true;
  newMessage.isPaused = false;
  
  if (!resume) {
    typeState.value = { active: true, paused: false, text: fullText, index: 0, msgIndex: messageIndex };
    newMessage.text = '';
  } else typeState.value.paused = false;

  typewriterTimer = setInterval(() => {
    if (typeState.value.paused) {
      clearInterval(typewriterTimer);
      newMessage.isTyping = false; newMessage.isPaused = true; isGenerating.value = false;
      return;
    }

    newMessage.text += typeState.value.text.charAt(typeState.value.index);
    typeState.value.index++;
    scrollToBottom();

    if (typeState.value.index >= typeState.value.text.length) {
      clearInterval(typewriterTimer);
      newMessage.isTyping = false; newMessage.isPaused = false; isGenerating.value = false;
      typeState.value.active = false;
      
      if (fullText.includes("⚠️") || fullText.toLowerCase().includes("erro")) newMessage.expression = 'confused';
      else if (fullText.length < 50) newMessage.expression = 'happy';
    }
  }, 10);
};

const stopGeneration = () => { if (typewriterTimer) typeState.value.paused = true; };
const resumeGeneration = (index: number) => { if (typeState.value.msgIndex === index && typeState.value.text) typeWriter(index, typeState.value.text, true); };

const chatTopics = computed(() => {
   return messages.value
     .map((msg, idx) => ({ ...msg, originalIndex: idx }))
     .filter(msg => msg.sender === 'user' && (msg.text || (msg.images && msg.images.length > 0)));
});

const scrollToMessage = (index: number) => {
   const el = document.getElementById('msg-' + index);
   if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
};

const startEdit = (index: number) => {
   messages.value[index].isEditing = true;
   messages.value[index].editText = messages.value[index].text;
   // Copia imagens existentes para o modo de edição
   messages.value[index].editImages = messages.value[index].images ? [...messages.value[index].images] : [];
};

const cancelEdit = (index: number) => { messages.value[index].isEditing = false; };

// FUNÇÃO MÁGICA DE COLAR (CTRL+V) IMAGENS NA EDIÇÃO
const handleEditPaste = (e: ClipboardEvent, index: number) => {
  if (e.clipboardData && e.clipboardData.items) {
    for (const item of e.clipboardData.items) {
      if (item.type.indexOf('image') === 0) {
        const file = item.getAsFile();
        if (file) {
          const reader = new FileReader();
          reader.onload = (evt) => {
             const imgStr = evt.target?.result as string;
             if (!messages.value[index].editImages) messages.value[index].editImages = [];
             messages.value[index].editImages!.push(imgStr); 
          };
          reader.readAsDataURL(file);
        }
      }
    }
  }
};

const submitEdit = (index: number) => {
   const newText = messages.value[index].editText || '';
   const newImages = messages.value[index].editImages || [];
   
   messages.value = messages.value.slice(0, index); 
   handleSendMessage({ text: newText, images: newImages });
};

const handleSendMessage = async (payload: { text: string; images: string[] }) => {
  isUserScrolledUp.value = false;
  
  messages.value.push({ sender: 'user', text: payload.text, images: payload.images });
  scrollToBottom();

  const botMsgIndex = messages.value.length;
  messages.value.push({ sender: 'bot', text: '', isTyping: true, expression: 'analytical' });

  try {
    const promptComEmojis = payload.text + "\n\n(Instrução do Sistema: Responda a esta mensagem usando uma linguagem clara, profissional, mas inclua emojis relevantes de forma natural para tornar o texto mais amigável e empático).";

    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: promptComEmojis, images: payload.images })
    });

    if (!response.ok) throw new Error("Erro de Servidor");
    
    const data = await response.json();
    
    messages.value[botMsgIndex].expression = 'neutral';
    typeWriter(botMsgIndex, data.reply);
  } catch (error) {
    messages.value[botMsgIndex].isTyping = false;
    messages.value[botMsgIndex].expression = 'confused'; 
    messages.value[botMsgIndex].text = "⚠️ Ocorreu um erro ao comunicar com a IA. Verifique se o backend Python está a correr.";
    isGenerating.value = false;
  }
};

onMounted(() => { scrollToBottom(); });
</script>

<style scoped>
/* Tipografia Profissional */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Open+Sans:wght@400;500;600;700&display=swap');

/* Melhorias na Renderização do Markdown */
:deep(.markdown-body) { font-family: 'Open Sans', sans-serif; color: #334155; font-size: 15px; }
:deep(.dark .markdown-body) { color: #cbd5e1; }
:deep(.markdown-body p) { margin-bottom: 1.25rem; line-height: 1.75; }
:deep(.markdown-body p:last-child) { margin-bottom: 0; }

:deep(.markdown-body table) { 
  width: 100%; border-collapse: separate; border-spacing: 0; margin: 1.5rem 0; 
  border-radius: 12px; overflow: hidden; font-size: 0.9rem; 
  border: 1px solid #e2e8f0; box-shadow: 0 1px 2px rgba(0,0,0,0.05); 
}
:deep(.dark .markdown-body table) { border-color: #1e293b; box-shadow: 0 1px 2px rgba(0,0,0,0.5); }
:deep(.markdown-body th), :deep(.markdown-body td) { border-bottom: 1px solid #f1f5f9; padding: 12px 16px; text-align: left; }
:deep(.dark .markdown-body th), :deep(.dark .markdown-body td) { border-bottom-color: #0f172a; }
:deep(.markdown-body th) { 
  font-family: 'Montserrat', sans-serif; background: #f8fafc; color: #475569; 
  font-weight: 700; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.05em; 
}
:deep(.dark .markdown-body th) { background: #0f172a; color: #94a3b8; }

:deep(.markdown-body ul), :deep(.markdown-body ol) { padding-left: 0; margin: 1.25rem 0; }
:deep(.markdown-body ul li) { position: relative; padding-left: 1.5rem; margin-bottom: 0.5rem; line-height: 1.6; }
:deep(.markdown-body ul li::before) { 
  content: '•'; position: absolute; left: 0.25rem; top: 0; 
  font-size: 1.2rem; color: #6366f1; font-weight: bold; line-height: 1.4;
}

:deep(.markdown-body strong) { color: #1e293b; font-weight: 700; }
:deep(.dark .markdown-body strong) { color: #f8fafc; }

:deep(.markdown-body h3) { 
  font-family: 'Montserrat', sans-serif; font-size: 1.15rem; font-weight: 700; 
  margin-top: 1.75rem; margin-bottom: 0.75rem; color: #0f172a; 
}
:deep(.dark .markdown-body h3) { color: #f8fafc; }

/* Scrollbar Customizada */
.custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.3); border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar:hover::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.5); }
.dark .custom-scrollbar:hover::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.2); }
</style>