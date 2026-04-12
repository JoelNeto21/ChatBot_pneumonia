<template>
  <div :class="['flex flex-col h-screen w-full text-slate-800 dark:text-slate-200 font-sans transition-colors duration-300', isDark ? 'bg-[#0f1115]' : 'bg-white', fontSizeClass]">
    
    <div v-if="zoomedImage" @click="zoomedImage = null" class="fixed inset-0 z-[100] bg-black/90 backdrop-blur-sm flex items-center justify-center p-4 cursor-zoom-out animate-in fade-in duration-200">
      <img :src="zoomedImage" class="max-w-full max-h-full object-contain rounded-lg shadow-2xl scale-100 animate-in zoom-in-95 duration-200" />
      <div class="absolute top-6 right-6 text-white/50 hover:text-white transition-colors">
        <i class="fas fa-times text-2xl"></i>
      </div>
    </div>

    <header :class="['h-16 w-full flex items-center justify-between px-4 md:px-8 backdrop-blur-md border-b fixed top-0 z-50 transition-colors', isDark ? 'bg-[#0f1115]/80 border-white/5' : 'bg-white/80 border-slate-100']">
      <NuxtLink to="/" class="flex items-center gap-3 group cursor-pointer text-decoration-none">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-indigo-500 to-violet-600 flex items-center justify-center text-white shadow-lg shadow-indigo-500/20 group-hover:scale-105 group-hover:rotate-3 transition-all">
          <i class="fas fa-lungs text-sm"></i>
        </div>
        <span class="font-extrabold text-[17px] tracking-tight group-hover:text-indigo-500 transition-colors" style="font-family: 'Montserrat', sans-serif;">
          PneumoAssist <span class="font-light opacity-60">IA</span>
        </span>
      </NuxtLink>
      
      <div class="flex items-center gap-3 md:gap-4">
        <div :class="['relative flex items-center rounded-full px-3 py-1.5 border transition-colors', isDark ? 'bg-white/5 border-white/10' : 'bg-slate-100 border-slate-200']">
          <i class="fas fa-globe text-indigo-500 text-xs mr-2"></i>
          <select v-model="currentLang" @change="handleLanguageChange" class="bg-transparent text-xs font-bold outline-none cursor-pointer appearance-none pr-4">
            <option value="pt-PT" class="text-slate-900">PT</option>
            <option value="en-US" class="text-slate-900">EN</option>
            <option value="es-ES" class="text-slate-900">ES</option>
            <option value="fr-FR" class="text-slate-900">FR</option>
          </select>
          <i class="fas fa-chevron-down absolute right-3 text-[10px] text-slate-400 pointer-events-none"></i>
        </div>

        <button @click="cycleFontSize" :class="['w-9 h-9 rounded-full flex items-center justify-center transition-colors', isDark ? 'hover:bg-white/5 text-slate-400' : 'hover:bg-slate-100 text-slate-500']" title="Ajustar Tamanho">
          <span class="font-bold font-serif text-sm">AA</span>
        </button>

        <button @click="toggleTheme" :class="['w-9 h-9 rounded-full flex items-center justify-center transition-colors', isDark ? 'hover:bg-white/5 text-amber-400' : 'hover:bg-slate-100 text-slate-500']" title="Mudar Tema">
          <i :class="isDark ? 'fas fa-sun' : 'fas fa-moon'"></i>
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
              <h3 class="font-extrabold text-3xl md:text-4xl mb-3 tracking-tight" style="font-family: 'Montserrat', sans-serif;">Pneumologia Clínica</h3>
              <p class="text-slate-500 dark:text-slate-400/80 max-w-md mx-auto text-[15px] leading-relaxed">
                Sou especialista exclusivo em vias respiratórias e pulmões. Descreva os sintomas ou anexe os exames do paciente para iniciar a análise.
              </p>
            </div>

            <div v-for="(msg, index) in messages" :key="index" :id="'msg-' + index" class="w-full relative flex flex-col group/message">
              
              <div v-if="msg.sender === 'bot'" class="flex gap-4 w-full animate-in slide-in-from-left-4 duration-300">
                <KoalaIcon :expression="msg.expression || 'neutral'" class="mt-1 flex-shrink-0" />
                
                <div class="flex-1 overflow-hidden min-w-0 pt-1">
                  <div class="flex items-center gap-2 mb-2">
                    <span class="font-bold text-[13px]" style="font-family: 'Montserrat', sans-serif;">PneumoAssist IA</span>
                    <i class="fas fa-certificate text-indigo-500 text-[10px]" title="IA Verificada"></i>
                  </div>
                  
                  <div class="leading-relaxed text-inherit">
                    <div class="markdown-body" v-html="renderMarkdown(msg.text)"></div>
                    
                    <div v-if="msg.isTyping" class="mt-3 flex items-center gap-2 text-indigo-400 text-sm font-medium animate-pulse">
                      <div class="flex gap-1">
                        <span class="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-bounce" style="animation-delay: 0s"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-bounce" style="animation-delay: 0.2s"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-bounce" style="animation-delay: 0.4s"></span>
                      </div>
                    </div>
                  </div>

                  <div v-if="!msg.isTyping && msg.text" class="flex flex-wrap items-center gap-1.5 mt-3 opacity-0 group-hover/message:opacity-100 transition-opacity duration-300">
                    
                    <button @click="toggleSpeech(msg.text)" :class="['w-8 h-8 rounded-full flex items-center justify-center transition-all', isSpeakingText === msg.text ? 'text-indigo-500 bg-indigo-50 dark:bg-indigo-500/10' : 'text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-indigo-500']" title="Ler Resposta">
                      <i :class="isSpeakingText === msg.text ? 'fas fa-volume-up animate-pulse' : 'fas fa-volume-down'"></i>
                    </button>
                    
                    <button @click="copyText(msg.text)" class="w-8 h-8 rounded-full flex items-center justify-center text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-slate-700 dark:hover:text-white transition-all" title="Copiar Texto">
                      <i class="fas fa-copy text-xs"></i>
                    </button>

                    <div class="w-px h-4 bg-slate-200 dark:bg-slate-700 mx-1"></div> <button @click="msg.liked = true" :class="['w-8 h-8 rounded-full flex items-center justify-center transition-all', msg.liked === true ? 'text-emerald-500 bg-emerald-50 dark:bg-emerald-500/10' : 'text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-emerald-500']" title="Gostei da Resposta">
                      <i class="fas fa-thumbs-up text-xs"></i>
                    </button>

                    <button @click="msg.liked = false" :class="['w-8 h-8 rounded-full flex items-center justify-center transition-all', msg.liked === false ? 'text-rose-500 bg-rose-50 dark:bg-rose-500/10' : 'text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-rose-500']" title="Não Gostei">
                      <i class="fas fa-thumbs-down text-xs"></i>
                    </button>

                    <button @click="shareMessage(msg.text)" class="w-8 h-8 rounded-full flex items-center justify-center text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-blue-500 transition-all" title="Compartilhar">
                      <i class="fas fa-share-nodes text-xs"></i>
                    </button>

                    <div v-if="index > 0" class="w-px h-4 bg-slate-200 dark:bg-slate-700 mx-1"></div> <button v-if="index > 0" @click="retryMessage(index)" class="w-8 h-8 rounded-full flex items-center justify-center text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-amber-500 transition-all" title="Tentar Novamente">
                      <i class="fas fa-rotate-right text-xs"></i>
                    </button>

                    <button v-if="index > 0" @click="continueGeneration()" class="px-3 h-8 rounded-full flex items-center gap-1.5 text-xs font-bold text-slate-400 hover:bg-slate-100 dark:hover:bg-white/10 hover:text-indigo-500 transition-all" title="Se o texto parou a meio, peça para continuar">
                      <i class="fas fa-play text-[10px]"></i> Continuar
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
                      class="w-full bg-transparent border-none focus:ring-0 resize-none text-[15px] p-0 no-scrollbar outline-none" 
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

                  <div v-else class="bg-slate-100 dark:bg-white/5 border border-transparent dark:border-white/5 rounded-3xl rounded-tr-sm px-5 py-4 shadow-sm break-words w-full overflow-wrap-anywhere">
                    <div v-if="msg.images && msg.images.length > 0" class="flex flex-wrap gap-2 mb-3">
                      <div v-for="(img, imgIdx) in msg.images" :key="imgIdx" class="relative group/img">
                        <img :src="img" @click="zoomedImage = img" class="h-16 w-16 md:h-20 md:w-20 object-cover rounded-xl border border-slate-200 dark:border-slate-700 cursor-zoom-in hover:opacity-80 transition-opacity shadow-sm" alt="Anexo" />
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

// ==========================================
// ESTADO E ACESSIBILIDADE
// ==========================================
const currentLang = ref('pt-PT');
const fontSize = ref('text-[15.5px]'); 
const isDark = ref(true);

const cycleFontSize = () => {
  if (fontSize.value === 'text-[14px]') fontSize.value = 'text-[15.5px]';
  else if (fontSize.value === 'text-[15.5px]') fontSize.value = 'text-[18px]';
  else fontSize.value = 'text-[14px]';
};
const fontSizeClass = computed(() => fontSize.value);

const toggleTheme = () => {
  isDark.value = !isDark.value;
  document.documentElement.classList.toggle('dark', isDark.value);
  if (typeof window !== 'undefined') {
    localStorage.setItem('theme', isDark.value ? 'dark' : 'light');
  }
};

const handleLanguageChange = () => {};

// ==========================================
// GESTÃO DO CHAT E MENSAGENS
// ==========================================
const scrollContainer = ref<HTMLElement | null>(null);
const isGenerating = ref(false);
const isUserScrolledUp = ref(false);
const zoomedImage = ref<string | null>(null);

// Interface Atualizada com opções de Like
interface Message {
  sender: 'user' | 'bot';
  text: string;
  expression?: 'neutral' | 'happy' | 'analytical' | 'confused'; 
  images?: string[]; 
  isTyping?: boolean;
  isEditing?: boolean;
  editText?: string;
  isHidden?: boolean; 
  liked?: boolean | null; // Adicionado para Gostei/Não Gostei
}

const messages = ref<Message[]>([
  { sender: 'bot', text: 'Olá! 👋 Sou o **PneumoAssist**, uma IA Clínica dedicada a Pneumologia.\n\nPosso ajudar a interpretar sintomas ou analisar exames médicos. Em que posso ser útil?', expression: 'happy', liked: null }
]);

const renderMarkdown = (text: string) => marked(text, { breaks: true, gfm: true }) as string;

// ==========================================
// SCROLL & UI
// ==========================================
const handleScroll = () => {
  if (!scrollContainer.value) return;
  const { scrollTop, scrollHeight, clientHeight } = scrollContainer.value;
  isUserScrolledUp.value = Math.ceil(scrollTop + clientHeight) < scrollHeight - 20;
};

const scrollToBottom = () => {
  if (isUserScrolledUp.value) return; 
  nextTick(() => { 
    if (scrollContainer.value) {
      scrollContainer.value.scrollTop = scrollContainer.value.scrollHeight; 
    }
  });
};

const forceScrollToBottom = () => {
  isUserScrolledUp.value = false;
  nextTick(() => { 
    if (scrollContainer.value) {
      scrollContainer.value.scrollTo({ top: scrollContainer.value.scrollHeight, behavior: 'smooth' }); 
    }
  });
};

// ==========================================
// TYPEWRITER EFFECT
// ==========================================
let typewriterTimer: any = null;
const typeState = ref({ paused: false });

const typeWriter = (messageIndex: number, fullText: string) => {
  isGenerating.value = true;
  const newMessage = messages.value[messageIndex];
  newMessage.isTyping = true;
  newMessage.text = ''; 
  typeState.value.paused = false;

  let i = 0;
  const charsPerTick = 2; 

  typewriterTimer = setInterval(() => {
    if (typeState.value.paused) {
      clearInterval(typewriterTimer);
      newMessage.isTyping = false; 
      isGenerating.value = false;
      return;
    }

    newMessage.text += fullText.slice(i, i + charsPerTick);
    i += charsPerTick;
    
    if (i % 10 === 0 && !isUserScrolledUp.value) scrollToBottom();

    if (i >= fullText.length) {
      clearInterval(typewriterTimer);
      newMessage.text = fullText; 
      newMessage.isTyping = false; 
      isGenerating.value = false;
      if (!isUserScrolledUp.value) scrollToBottom();
    }
  }, 15); 
};

const stopGeneration = () => { 
  if (typewriterTimer) typeState.value.paused = true; 
};

// ==========================================
// NOVAS AÇÕES: COPIAR, COMPARTILHAR, TENTAR DE NOVO
// ==========================================
const copyText = (text: string) => {
  if (typeof navigator !== 'undefined' && navigator.clipboard) {
    navigator.clipboard.writeText(text);
  }
};

const shareMessage = async (text: string) => {
  if (typeof navigator !== 'undefined' && navigator.share) {
    try {
      await navigator.share({
        title: 'PneumoAssist IA',
        text: text,
      });
    } catch (error) {
      console.log('Partilha cancelada ou falhou', error);
    }
  } else {
    // Fallback se não houver suporte à partilha nativa
    copyText(text);
    alert('Texto copiado para a área de transferência! O seu navegador não suporta partilha direta.');
  }
};

// ==========================================
// LÓGICA DE API SEPARADA (Para reutilização)
// ==========================================
const fetchAILogic = async (botMsgIndex: number, userText: string, userImages: string[]) => {
  messages.value[botMsgIndex].isTyping = true;
  messages.value[botMsgIndex].expression = 'analytical';
  
  const mapLang = { 'pt-PT': 'Português', 'en-US': 'Inglês', 'es-ES': 'Espanhol', 'fr-FR': 'Francês' };
  const targetLang = mapLang[currentLang.value as keyof typeof mapLang] || 'Português';

  const cleanMessage = userText + `\n\n[Sistema: Responda a esta análise obrigatoriamente no idioma ${targetLang}.]`;
  
  try {
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ 
        message: cleanMessage, 
        image: userImages && userImages.length > 0 ? userImages[0] : null 
      })
    });

    if (!response.ok) throw new Error("Erro de Servidor");
    const data = await response.json();
    
    messages.value[botMsgIndex].expression = 'neutral';
    typeWriter(botMsgIndex, data.reply);
  } catch (error) {
    messages.value[botMsgIndex].isTyping = false;
    messages.value[botMsgIndex].expression = 'confused'; 
    messages.value[botMsgIndex].text = "⚠️ **Erro de Conexão.**\nNão foi possível contactar os servidores da IA. Verifique se o backend está a correr.";
    isGenerating.value = false;
  }
};

// ==========================================
// ENVIAR MENSAGENS E CONTINUAR
// ==========================================
const handleSendMessage = async (payload: { text: string; images: string[] }) => {
  isUserScrolledUp.value = false;
  messages.value.push({ sender: 'user', text: payload.text, images: payload.images, isHidden: false });
  scrollToBottom();

  const botMsgIndex = messages.value.length;
  messages.value.push({ sender: 'bot', text: '', isTyping: true, liked: null });

  await fetchAILogic(botMsgIndex, payload.text, payload.images);
};

const retryMessage = (botIndex: number) => {
  if (isGenerating.value) return; // Bloqueia se já estiver a gerar algo
  
  // Procura a última mensagem do utilizador antes desta resposta do bot
  let userMsgIndex = botIndex - 1;
  while (userMsgIndex >= 0 && messages.value[userMsgIndex].sender !== 'user') {
    userMsgIndex--;
  }
  
  if (userMsgIndex < 0) return; // Segurança

  const userPayload = messages.value[userMsgIndex];
  
  // Limpa o texto do bot e reinicia o estado
  messages.value[botIndex].text = '';
  messages.value[botIndex].liked = null;
  
  fetchAILogic(botIndex, userPayload.text, userPayload.images || []);
};

const continueGeneration = () => {
  // Envia automaticamente um comando para a IA continuar
  handleSendMessage({ text: "A sua última mensagem foi interrompida. Continue de onde parou, por favor.", images: [] });
};

// ==========================================
// EDIÇÃO DE MENSAGENS DO UTILIZADOR
// ==========================================
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

// ==========================================
// TEXT-TO-SPEECH
// ==========================================
const isSpeakingText = ref<string | null>(null);

const toggleSpeech = (text: string) => {
  if (typeof window === 'undefined' || !window.speechSynthesis) {
    alert("O seu navegador não suporta leitura de voz.");
    return;
  }
  
  const synth = window.speechSynthesis;

  if (isSpeakingText.value === text) {
    synth.cancel();
    isSpeakingText.value = null;
    return;
  }
  
  synth.cancel(); 
  
  const cleanText = text.replace(/[*_#`]/g, '');
  const utterance = new SpeechSynthesisUtterance(cleanText);
  utterance.lang = currentLang.value;
  utterance.rate = 1.0;
  
  utterance.onend = () => { isSpeakingText.value = null; };
  utterance.onerror = () => { isSpeakingText.value = null; };
  
  isSpeakingText.value = text;
  synth.speak(utterance);
};

// ==========================================
// LIFECYCLE HOOKS
// ==========================================
onMounted(() => {
  const storedTheme = localStorage.getItem('theme');
  if (storedTheme === 'dark' || (!storedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDark.value = true;
    document.documentElement.classList.add('dark');
  } else {
    isDark.value = false;
    document.documentElement.classList.remove('dark');
  }

  scrollToBottom();
});

onUnmounted(() => {
  if (typeof window !== 'undefined' && window.speechSynthesis) {
    window.speechSynthesis.cancel();
  }
  if (typewriterTimer) clearInterval(typewriterTimer);
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Open+Sans:wght@400;500;600;700&display=swap');

.no-scrollbar::-webkit-scrollbar { display: none; }
.no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }

:deep(.markdown-body) { 
  font-family: 'Open Sans', sans-serif; 
  font-size: inherit; 
  line-height: 1.7; 
  color: inherit;
}

:deep(.markdown-body p) { margin-bottom: 1rem; }
:deep(.markdown-body p:last-child) { margin-bottom: 0; }
:deep(.markdown-body strong) { font-weight: 700; color: #4f46e5; }
:deep(.dark .markdown-body strong) { color: #818cf8; }
:deep(.markdown-body ul) { list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1rem; }
:deep(.markdown-body ol) { list-style-type: decimal; padding-left: 1.5rem; margin-bottom: 1rem; }
:deep(.markdown-body li) { margin-bottom: 0.25rem; }

/* Estilos para Tabelas */
:deep(.markdown-body table) {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1rem;
  font-size: 0.95em;
  border-radius: 8px;
  overflow: hidden; /* Garante que as bordas arredondadas funcionem */
}

:deep(.markdown-body th) {
  background-color: rgba(79, 70, 229, 0.1); /* Indigo suave */
  font-weight: 700;
  text-align: left;
  padding: 12px;
  border: 1px solid rgba(79, 70, 229, 0.2);
}

:deep(.dark .markdown-body th) {
  background-color: rgba(129, 140, 248, 0.1);
  border-color: rgba(255, 255, 255, 0.1);
}

:deep(.markdown-body td) {
  padding: 10px 12px;
  border: 1px solid #e2e8f0;
}

:deep(.dark .markdown-body td) {
  border-color: rgba(255, 255, 255, 0.05);
}

:deep(.markdown-body tr:nth-child(even)) {
  background-color: rgba(0, 0, 0, 0.02);
}

:deep(.dark .markdown-body tr:nth-child(even)) {
  background-color: rgba(255, 255, 255, 0.02);
}

/* Scroll horizontal em telas pequenas */
:deep(.markdown-body table) {
  display: block;
  overflow-x: auto;
  white-space: nowrap;
}

/* Títulos de Seções */
:deep(.markdown-body h2) {
  font-family: 'Montserrat', sans-serif;
  font-size: 1.4rem;
  font-weight: 800;
  color: #4f46e5;
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
  border-bottom: 2px solid rgba(79, 70, 229, 0.1);
  padding-bottom: 4px;
  text-transform: uppercase; /* Força títulos principais em maiúsculas */
  letter-spacing: -0.02em;
}

:deep(.dark .markdown-body h2) {
  color: #818cf8;
  border-bottom-color: rgba(255, 255, 255, 0.05);
}

:deep(.markdown-body h3) {
  font-family: 'Montserrat', sans-serif;
  font-size: 1.1rem;
  font-weight: 700;
  margin-top: 1.2rem;
  color: #1e293b;
}

:deep(.dark .markdown-body h3) {
  color: #f1f5f9;
}

/* Melhoria no corpo do texto */
:deep(.markdown-body) {
  line-height: 1.8;
  letter-spacing: 0.01em;
}
</style>