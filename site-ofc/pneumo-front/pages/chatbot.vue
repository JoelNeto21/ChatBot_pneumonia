<template>
  <div :class="['flex flex-col h-screen w-full bg-white dark:bg-[#0f1115] text-slate-800 dark:text-slate-200 font-sans transition-colors duration-300', fontSizeClass]">
    
    <div v-if="zoomedImage" @click="zoomedImage = null" class="fixed inset-0 z-[100] bg-black/90 backdrop-blur-sm flex items-center justify-center p-4 cursor-zoom-out animate-in fade-in duration-200">
      <img :src="zoomedImage" class="max-w-full max-h-full object-contain rounded-lg shadow-2xl scale-100 animate-in zoom-in-95 duration-200" />
      <div class="absolute top-6 right-6 text-white/50 hover:text-white transition-colors">
        <i class="fas fa-times text-2xl"></i>
      </div>
    </div>

    <header class="h-16 w-full flex items-center justify-between px-4 md:px-8 bg-white/80 dark:bg-[#0f1115]/80 backdrop-blur-md border-b border-slate-100 dark:border-white/5 fixed top-0 z-50 transition-colors">
      <a href="/" class="flex items-center gap-3 group cursor-pointer text-decoration-none">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-indigo-500 to-violet-600 flex items-center justify-center text-white shadow-lg shadow-indigo-500/20 group-hover:scale-105 group-hover:rotate-3 transition-all">
          <i class="fas fa-lungs text-sm"></i>
        </div>
        <span class="font-extrabold text-[17px] text-slate-800 dark:text-white tracking-tight group-hover:text-indigo-500 transition-colors" style="font-family: 'Montserrat', sans-serif;">
          PneumoAssist <span class="font-light opacity-60">IA</span>
        </span>
      </a>
      
      <div class="flex items-center gap-3 md:gap-4">
        <div class="relative flex items-center bg-slate-100 dark:bg-white/5 rounded-full px-3 py-1.5 border border-slate-200 dark:border-white/10">
          <i class="fas fa-globe text-indigo-500 text-xs mr-2"></i>
          <select v-model="currentLang" class="bg-transparent text-xs font-bold text-slate-600 dark:text-slate-300 outline-none cursor-pointer appearance-none pr-4">
            <option value="pt-PT">PT</option>
            <option value="en-US">EN</option>
            <option value="es-ES">ES</option>
            <option value="fr-FR">FR</option>
          </select>
          <i class="fas fa-chevron-down absolute right-3 text-[10px] text-slate-400 pointer-events-none"></i>
        </div>

        <button @click="cycleFontSize" class="w-9 h-9 rounded-full hover:bg-slate-100 dark:hover:bg-white/5 flex items-center justify-center text-slate-500 dark:text-slate-400 transition-colors" title="Ajustar Tamanho do Texto">
          <span class="font-bold font-serif text-sm">AA</span>
        </button>

        <button @click="toggleTheme" class="w-9 h-9 rounded-full hover:bg-slate-100 dark:hover:bg-white/5 flex items-center justify-center text-slate-500 dark:text-slate-400 transition-colors" title="Mudar Tema">
          <i :class="isDark ? 'fas fa-sun text-amber-400' : 'fas fa-moon'"></i>
        </button>
      </div>
    </header>

    <main class="flex-1 flex relative overflow-hidden pt-16">
      
      <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] bg-opacity-[0.10] dark:opacity-[0.03] pointer-events-none"></div>

      <div class="flex-1 flex flex-col relative overflow-hidden z-10 w-full max-w-4xl mx-auto">
        
        <div ref="scrollContainer" @scroll="handleScroll" class="flex-1 overflow-y-auto px-4 md:px-8 py-8 no-scrollbar scroll-smooth">
          <div class="space-y-8 md:space-y-12 pb-36">
            
            <div v-if="messages.length <= 1" class="flex flex-col items-center py-12 md:py-20 text-center animate-in fade-in zoom-in duration-700">
              <div class="relative mb-6">
                <div class="absolute inset-0 bg-indigo-500/20 blur-3xl rounded-full"></div>
                <KoalaIcon expression="happy" class="scale-125 md:scale-150 relative z-10 drop-shadow-xl" />
              </div>
              <h3 class="text-slate-800 dark:text-white font-extrabold text-3xl md:text-4xl mb-3 tracking-tight" style="font-family: 'Montserrat', sans-serif;">Pneumologia Clínica</h3>
              <p class="text-slate-500 dark:text-slate-400/80 max-w-md mx-auto text-[15px] leading-relaxed">Sou especialista exclusivo em vias respiratórias e pulmões. Descreva os sintomas ou anexe os exames do paciente para iniciar a análise.</p>
            </div>

            <div v-for="(msg, index) in messages" :key="index" :id="'msg-' + index" class="w-full relative flex flex-col group/message">
              
              <div v-if="msg.sender === 'bot'" class="flex gap-4 w-full animate-in slide-in-from-left-4 duration-300">
                <KoalaIcon :expression="msg.expression || 'neutral'" class="mt-1 flex-shrink-0" />
                
                <div class="flex-1 overflow-hidden min-w-0 pt-1">
                  <div class="flex items-center gap-2 mb-2">
                    <span class="font-bold text-[13px] text-slate-800 dark:text-slate-200" style="font-family: 'Montserrat', sans-serif;">PneumoAssist IA</span>
                    <i class="fas fa-certificate text-indigo-500 text-[10px]" title="IA Verificada"></i>
                  </div>
                  
                  <div class="text-slate-700 dark:text-slate-300 leading-relaxed text-inherit">
                    <div class="markdown-body" v-html="renderMarkdown(msg.text)"></div>
                    
                    <div v-if="msg.isTyping" class="mt-3 flex items-center gap-2 text-indigo-400 text-sm font-medium animate-pulse">
                      <div class="flex gap-1">
                        <span class="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-bounce" style="animation-delay: 0s"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-bounce" style="animation-delay: 0.2s"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-bounce" style="animation-delay: 0.4s"></span>
                      </div>
                    </div>
                  </div>

                  <div v-if="!msg.isTyping && msg.text" class="flex items-center gap-1.5 mt-3 opacity-0 group-hover/message:opacity-100 transition-opacity duration-300">
                    <button @click="toggleSpeech(msg.text)" :class="['w-8 h-8 rounded-full flex items-center justify-center transition-all', isSpeakingText === msg.text ? 'text-indigo-500 bg-indigo-50 dark:bg-indigo-500/10' : 'text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-indigo-500']" title="Ler Resposta">
                      <i :class="isSpeakingText === msg.text ? 'fas fa-volume-up animate-pulse' : 'fas fa-volume-down'"></i>
                    </button>
                    <button @click="copyText(msg.text)" class="w-8 h-8 rounded-full flex items-center justify-center text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-slate-700 dark:hover:text-white transition-all" title="Copiar">
                      <i class="fas fa-copy text-xs"></i>
                    </button>
                    <button @click="handleAction(msg, 'like')" :class="['w-8 h-8 rounded-full flex items-center justify-center transition-all', msg.action === 'like' ? 'text-green-500 bg-green-50 dark:bg-green-500/10' : 'text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-green-500']" title="Boa resposta">
                      <i class="fas fa-thumbs-up text-xs"></i>
                    </button>
                    <button @click="handleAction(msg, 'dislike')" :class="['w-8 h-8 rounded-full flex items-center justify-center transition-all', msg.action === 'dislike' ? 'text-rose-500 bg-rose-50 dark:bg-rose-500/10' : 'text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-rose-500']" title="Resposta incorreta">
                      <i class="fas fa-thumbs-down text-xs"></i>
                    </button>
                  </div>
                </div>
              </div>

              <div v-else class="flex justify-end w-full group/user relative mt-2 mb-2">
                <div class="max-w-[90%] md:max-w-[75%] flex flex-col items-end">
                  
                  <div class="flex items-center gap-2 mb-1.5 opacity-0 group-hover/user:opacity-100 transition-opacity duration-300 mr-1">
                    <button @click="msg.isHidden = !msg.isHidden" class="text-[10px] uppercase font-bold text-slate-400 hover:text-indigo-500 tracking-wider flex items-center gap-1">
                      <i :class="msg.isHidden ? 'fas fa-eye' : 'fas fa-eye-slash'"></i> {{ msg.isHidden ? 'Mostrar' : 'Ocultar' }}
                    </button>
                    <button v-if="!msg.isHidden" @click="startEdit(index)" class="text-[10px] uppercase font-bold text-slate-400 hover:text-indigo-500 tracking-wider flex items-center gap-1 ml-2">
                      <i class="fas fa-pen"></i> Editar
                    </button>
                  </div>

                  <div v-if="msg.isEditing" class="w-full min-w-[280px] bg-white dark:bg-slate-900/80 backdrop-blur border border-indigo-500/50 p-3 rounded-2xl shadow-xl animate-in zoom-in-95">
                    <textarea 
                      v-model="msg.editText" 
                      class="w-full bg-transparent border-none focus:ring-0 text-slate-800 dark:text-white resize-none text-[15px] p-0 no-scrollbar" 
                      rows="3"
                    ></textarea>
                    <div class="flex justify-end gap-2 mt-2">
                      <button @click="cancelEdit(index)" class="px-3 py-1.5 text-xs text-slate-500 hover:bg-slate-100 dark:hover:bg-white/10 rounded-lg font-semibold transition-colors">Cancelar</button>
                      <button @click="submitEdit(index)" class="px-3 py-1.5 text-xs bg-indigo-500 text-white rounded-lg font-semibold hover:bg-indigo-600 transition-colors">Guardar</button>
                    </div>
                  </div>

                  <div v-else-if="msg.isHidden" @click="msg.isHidden = false" class="bg-slate-100 dark:bg-white/5 border border-slate-200 dark:border-white/10 text-slate-500 dark:text-slate-400 px-4 py-2 rounded-2xl rounded-tr-sm text-sm cursor-pointer hover:bg-slate-200 dark:hover:bg-white/10 transition-colors flex items-center gap-2">
                    <i class="fas fa-comment-dots"></i> Mensagem ocultada
                  </div>

                  <div v-else class="bg-slate-100 dark:bg-white/5 border border-transparent dark:border-white/5 text-slate-800 dark:text-slate-200 rounded-3xl rounded-tr-sm px-5 py-4 shadow-sm break-words w-full overflow-wrap-anywhere" style="word-break: break-word;">
                    
                    <div v-if="msg.images && msg.images.length > 0" class="flex flex-wrap gap-2 mb-3">
                      <div v-for="(img, imgIdx) in msg.images" :key="imgIdx" class="relative group/img">
                        <img :src="img" @click="zoomedImage = img" class="h-16 w-16 md:h-20 md:w-20 object-cover rounded-xl border border-slate-200 dark:border-slate-700 cursor-zoom-in hover:opacity-80 transition-opacity shadow-sm" alt="Anexo" />
                        <div class="absolute inset-0 bg-black/40 opacity-0 group-hover/img:opacity-100 rounded-xl pointer-events-none transition-opacity flex items-center justify-center">
                          <i class="fas fa-search-plus text-white drop-shadow"></i>
                        </div>
                      </div>
                    </div>

                    <p v-if="msg.text" class="text-inherit leading-relaxed whitespace-pre-wrap font-medium">{{ msg.text }}</p>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <button v-show="isUserScrolledUp" @click="forceScrollToBottom" class="absolute bottom-28 right-6 w-10 h-10 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-indigo-500 rounded-full shadow-lg flex items-center justify-center hover:scale-110 transition-all z-40 animate-bounce">
          <i class="fas fa-arrow-down text-sm"></i>
        </button>

        <div class="relative z-30 pb-4">
          <ChatInput 
            :is-generating="isGenerating"
            @sendMessage="handleSendMessage" 
            @stopGeneration="stopGeneration"
          />
        </div>
      </div>
      
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, nextTick, onMounted, onUnmounted } from 'vue';
import { marked } from 'marked';
import ChatInput from '~/components/ChatInput.vue';
import KoalaIcon from '~/components/KoalaIcon.vue'; 

// --- Configurações de Acessibilidade e Idioma ---
const currentLang = ref('pt-PT');
const fontSize = ref('text-[15.5px]'); 

const cycleFontSize = () => {
  if (fontSize.value === 'text-[14px]') fontSize.value = 'text-[15.5px]';
  else if (fontSize.value === 'text-[15.5px]') fontSize.value = 'text-[18px]';
  else fontSize.value = 'text-[14px]';
};

const fontSizeClass = computed(() => fontSize.value);

const isDark = ref(true);
const toggleTheme = () => {
  isDark.value = !isDark.value;
  document.documentElement.classList.toggle('dark', isDark.value);
};

// --- Estado do Chat ---
const scrollContainer = ref<HTMLElement | null>(null);
const isGenerating = ref(false);
const isUserScrolledUp = ref(false);
const zoomedImage = ref<string | null>(null);

// --- Leitor de Voz (Text-to-Speech) ---
const isSpeakingText = ref<string | null>(null);
const synth = typeof window !== 'undefined' ? window.speechSynthesis : null;

const toggleSpeech = (text: string) => {
  if (!synth) return alert("O seu navegador não suporta leitura de voz.");
  
  if (isSpeakingText.value === text) {
    synth.cancel();
    isSpeakingText.value = null;
    return;
  }
  
  synth.cancel(); // Para leitura anterior
  
  // Limpa caracteres especiais do Markdown para ler de forma limpa
  const cleanText = text.replace(/[*_#`]/g, '');
  const utterance = new SpeechSynthesisUtterance(cleanText);
  utterance.lang = currentLang.value;
  utterance.rate = 1.0;
  
  utterance.onend = () => { isSpeakingText.value = null; };
  utterance.onerror = () => { isSpeakingText.value = null; };
  
  isSpeakingText.value = text;
  synth.speak(utterance);
};

// Pára a voz se o componente for destruído
onUnmounted(() => { if (synth) synth.cancel(); });

interface Message {
  sender: 'user' | 'bot';
  text: string;
  expression?: 'neutral' | 'happy' | 'analytical' | 'confused'; 
  images?: string[]; 
  isTyping?: boolean;
  isPaused?: boolean;
  isEditing?: boolean;
  editText?: string;
  isHidden?: boolean; 
  action?: 'like' | 'dislike' | null; 
}

const messages = ref<Message[]>([
  { sender: 'bot', text: 'Olá! 👋 Sou o **PneumoAssist**, uma IA Clínica exclusivamente dedicada a Pneumologia. \n\nPosso interpretar sintomas respiratórios ou analisar exames (como Raios-X ou TAC do tórax). Em que lhe posso ser útil hoje? 🫁', expression: 'happy' }
]);

const renderMarkdown = (text: string) => marked(text, { breaks: true, gfm: true }) as string;

const handleScroll = () => {
  if (!scrollContainer.value) return;
  const { scrollTop, scrollHeight, clientHeight } = scrollContainer.value;
  isUserScrolledUp.value = Math.ceil(scrollTop + clientHeight) < scrollHeight - 20;
};

const scrollToBottom = () => {
  if (isUserScrolledUp.value) return; 
  nextTick(() => { if (scrollContainer.value) scrollContainer.value.scrollTop = scrollContainer.value.scrollHeight; });
};

const forceScrollToBottom = () => {
  isUserScrolledUp.value = false;
  nextTick(() => { if (scrollContainer.value) scrollContainer.value.scrollTo({ top: scrollContainer.value.scrollHeight, behavior: 'smooth' }); });
};

let typewriterTimer: any = null;
const typeState = ref({ active: false, paused: false, text: '', index: 0, msgIndex: -1 });

const typeWriter = (messageIndex: number, fullText: string) => {
  isGenerating.value = true;
  const newMessage = messages.value[messageIndex];
  newMessage.isTyping = true;
  newMessage.text = ''; 
  typeState.value = { active: true, paused: false, text: fullText, index: 0, msgIndex: messageIndex }; 

  typewriterTimer = setInterval(() => {
    if (typeState.value.paused) {
      clearInterval(typewriterTimer);
      newMessage.isTyping = false; isGenerating.value = false;
      return;
    }

    newMessage.text += typeState.value.text.charAt(typeState.value.index);
    typeState.value.index++;
    
    if (!isUserScrolledUp.value) scrollToBottom();

    if (typeState.value.index >= typeState.value.text.length) {
      clearInterval(typewriterTimer);
      newMessage.isTyping = false; isGenerating.value = false;
      if (!isUserScrolledUp.value) scrollToBottom();
    }
  }, 10); 
};

const stopGeneration = () => { if (typewriterTimer) typeState.value.paused = true; };

const startEdit = (index: number) => {
   messages.value[index].isEditing = true;
   messages.value[index].editText = messages.value[index].text;
};
const cancelEdit = (index: number) => { messages.value[index].isEditing = false; };
const submitEdit = (index: number) => {
   const newText = messages.value[index].editText || '';
   messages.value = messages.value.slice(0, index); 
   handleSendMessage({ text: newText, images: [] }); 
};

const copyText = (text: string) => navigator.clipboard.writeText(text);

const handleAction = (msg: Message, type: 'like' | 'dislike') => {
  msg.action = msg.action === type ? null : type;
};

// --- Envio de Mensagem com "Blindagem Médica" ---
const handleSendMessage = async (payload: { text: string; images: string[] }) => {
  isUserScrolledUp.value = false;
  messages.value.push({ sender: 'user', text: payload.text, images: payload.images, isHidden: false });
  scrollToBottom();

  const botMsgIndex = messages.value.length;
  messages.value.push({ sender: 'bot', text: '', isTyping: true, expression: 'analytical' });

  // SISTEMA DE BLINDAGEM - Obriga a IA a respeitar limites e a ler ficheiros
  const mapLang = { 'pt-PT': 'Português de Portugal', 'en-US': 'Inglês', 'es-ES': 'Espanhol', 'fr-FR': 'Francês' };
  const targetLang = mapLang[currentLang.value as keyof typeof mapLang];

  const systemPrompt = `\n\n[INSTRUÇÃO ESTRITA DE SISTEMA PARA A IA: 
1. O TEU NOME É PNEUMOASSIST. Tu és uma IA MÉDICA ESTRITAMENTE FOCADA EM PNEUMOLOGIA e doenças respiratórias.
2. É ABSOLUTAMENTE PROIBIDO responder a perguntas sobre matemática, animais de estimação, computadores, jogos ou qualquer outro assunto não-médico. Se o utilizador tentar mudar de assunto, recusa educadamente e informa que a tua programação apenas te permite analisar questões respiratórias e pulmonares.
3. Se o utilizador enviou uma matriz de "images" (imagens) neste payload, tens de assumir obrigatoriamente que essas imagens são exames médicos de diagnóstico (Radiografias de Tórax, TC, Espirometrias, etc.) e tens de inferir/analisar as imagens se tiveres capacidades multimodais.
4. Responde OBRIGATORIAMENTE no idioma: ${targetLang}.
5. Sê empático e usa o formato Markdown nas respostas.]`;
  
  try {
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      // Enviamos as imagens e o texto juntamente com a regra restrita
      body: JSON.stringify({ message: payload.text + systemPrompt, images: payload.images })
    });

    if (!response.ok) throw new Error("Erro de Servidor");
    const data = await response.json();
    
    messages.value[botMsgIndex].expression = 'neutral';
    typeWriter(botMsgIndex, data.reply);
  } catch (error) {
    messages.value[botMsgIndex].isTyping = false;
    messages.value[botMsgIndex].expression = 'confused'; 
    messages.value[botMsgIndex].text = "⚠️ Não foi possível estabelecer ligação com os servidores clínicos. Por favor, tente novamente mais tarde.";
    isGenerating.value = false;
  }
};

onMounted(() => { scrollToBottom(); });
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Open+Sans:wght@400;500;600;700&display=swap');

.no-scrollbar::-webkit-scrollbar { display: none; }
.no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }

:deep(.markdown-body) { 
  font-family: 'Open Sans', sans-serif; 
  font-size: inherit; /* Herda o tamanho da fonte controlado pela acessibilidade */
  line-height: 1.7; 
  color: inherit;
}

:deep(.markdown-body p) { margin-bottom: 1.25rem; }
:deep(.markdown-body p:last-child) { margin-bottom: 0; }
:deep(.markdown-body strong) { font-weight: 700; color: #4f46e5; }
:deep(.dark .markdown-body strong) { color: #818cf8; }
:deep(.markdown-body ul) { list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1.25rem; margin-top: 0.5rem; }
:deep(.markdown-body ol) { list-style-type: decimal; padding-left: 1.5rem; margin-bottom: 1.25rem; margin-top: 0.5rem; }
:deep(.markdown-body li) { margin-bottom: 0.5rem; line-height: 1.6; }
</style>