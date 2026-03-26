<template>
  <div v-show="isOpen" @click="$emit('toggle')" class="md:hidden fixed inset-0 bg-slate-900/40 dark:bg-slate-900/80 backdrop-blur-sm z-40 transition-opacity duration-300"></div>

  <aside :class="[ 
      'fixed md:relative top-0 left-0 h-full z-50 transition-all duration-300 ease-in-out flex-shrink-0',
      'bg-white/95 dark:bg-slate-950/95 border-r border-slate-100 dark:border-slate-800 backdrop-blur-xl shadow-2xl md:shadow-none flex flex-col',
      isOpen ? 'w-80 translate-x-0' : 'w-0 -translate-x-full md:translate-x-0 border-transparent overflow-hidden'
    ]" style="font-family: 'Open Sans', sans-serif;">
    <div class="w-80 h-full flex flex-col p-6 overflow-y-auto custom-scrollbar">
      
      <div class="flex items-center justify-between mb-8 px-1 pb-5 border-b border-slate-100 dark:border-slate-800/80">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gradient-to-br from-indigo-500 to-indigo-600 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-500/30 relative">
            <i class="fas fa-lungs text-white text-lg relative z-10"></i>
            <div class="absolute inset-0 bg-white/20 rounded-xl animate-pulse"></div>
          </div>
          <div>
            <span class="block font-extrabold text-xl leading-tight tracking-tight text-slate-950 dark:text-white" style="font-family: 'Montserrat', sans-serif;">PneumoAssist</span>
            <span class="text-[10px] text-indigo-600 dark:text-indigo-400 font-bold uppercase tracking-widest flex items-center gap-1.5 mt-0.5">
              <i class="fas fa-heart-pulse animate-pulse"></i> IA Clínica Integrada
            </span>
          </div>
        </div>
        <button @click="$emit('toggle')" class="w-8 h-8 flex items-center justify-center rounded-xl text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-indigo-500 transition-all">
          <i class="fas fa-chevron-left"></i>
        </button>
      </div>
      
      <nav class="space-y-6 flex-1 flex flex-col">
        
        <div class="space-y-3">
          <h2 class="text-[10px] font-extrabold text-slate-400 dark:text-slate-500 uppercase tracking-widest px-2" style="font-family: 'Montserrat', sans-serif;">Assistente Principal</h2>
          <div class="flex items-center gap-4 p-3.5 rounded-2xl bg-slate-50 dark:bg-slate-900/50 border border-slate-100 dark:border-slate-800 shadow-sm transition-all group">
            <div class="w-12 h-12 flex-shrink-0 -mt-1 drop-shadow-md">
              <KoalaIcon expression="happy" />
            </div>
            <div>
              <span class="block font-bold text-slate-900 dark:text-white text-[15px]" style="font-family: 'Montserrat', sans-serif;">PneumoAssist IA</span>
              <span class="block text-emerald-600 dark:text-emerald-400 font-bold text-[10px] flex items-center gap-1.5 mt-0.5">
                <i class="fas fa-circle text-[6px] animate-pulse"></i> Online e Pronta
              </span>
            </div>
          </div>
        </div>

        <div class="space-y-1">
           <NuxtLink to="/" class="flex items-center gap-3.5 w-full text-left px-3 py-3 rounded-xl bg-transparent hover:bg-slate-50 dark:hover:bg-slate-900 text-slate-600 dark:text-slate-300 font-bold text-[13px] transition-colors group">
            <div class="w-8 h-8 rounded-lg bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-slate-500 group-hover:text-indigo-500 transition-colors shadow-sm">
              <i class="fas fa-home"></i>
            </div>
            Painel Principal
          </NuxtLink>

          <button @click="toggleTheme" class="flex items-center gap-3.5 w-full text-left px-3 py-3 rounded-xl bg-transparent hover:bg-slate-50 dark:hover:bg-slate-900 text-slate-600 dark:text-slate-300 font-bold text-[13px] transition-colors group">
            <div class="w-8 h-8 rounded-lg bg-slate-100 dark:bg-slate-800 flex items-center justify-center transition-colors shadow-sm">
              <i :class="['fas transition-colors duration-500', isDark ? 'fa-sun text-amber-500' : 'fa-moon text-indigo-500']"></i>
            </div>
            {{ isDark ? 'Modo de Leitura Claro' : 'Modo Contraste Escuro' }}
          </button>
        </div>

        <div class="space-y-3 pt-4 border-t border-slate-100 dark:border-slate-800/50">
          <h2 class="text-[10px] font-extrabold text-slate-400 dark:text-slate-500 uppercase tracking-widest px-2" style="font-family: 'Montserrat', sans-serif;">Sessões Recentes</h2>
          <div class="space-y-2">
            <div class="flex items-center justify-between px-3 py-2 rounded-xl border border-dashed border-slate-200 dark:border-slate-800 opacity-60 hover:opacity-100 transition-opacity cursor-pointer">
              <div class="flex items-center gap-3">
                <i class="fas fa-file-medical text-slate-400 text-xs"></i>
                <span class="text-xs font-semibold text-slate-600 dark:text-slate-300">Análise Raio-X Tórax</span>
              </div>
              <span class="text-[9px] font-bold text-slate-400">Ontem</span>
            </div>
          </div>
        </div>

        <div class="mt-4 p-4 rounded-2xl bg-slate-800 text-white shadow-inner relative overflow-hidden group">
          <div class="absolute -right-4 -top-4 text-slate-700/30 text-6xl group-hover:rotate-12 transition-transform duration-700 pointer-events-none">
            <i class="fas fa-microchip"></i>
          </div>
          <div class="relative z-10 space-y-3">
            <div class="flex justify-between items-end">
              <div>
                <span class="block text-[9px] font-bold text-slate-400 uppercase tracking-widest">Motor de Inferência</span>
                <span class="block text-xs font-extrabold text-emerald-400 mt-0.5 flex items-center gap-1.5">
                  <i class="fas fa-signal-stream"></i> Latência: 14ms
                </span>
              </div>
              <span class="text-[10px] font-bold bg-white/10 px-2 py-1 rounded-md text-slate-300">v2.4.1</span>
            </div>
            <div>
              <div class="flex justify-between text-[10px] font-bold text-slate-300 mb-1.5">
                <span>Precisão Llama 3.2</span>
                <span class="text-indigo-300">99.8%</span>
              </div>
              <div class="w-full h-1.5 bg-slate-900 rounded-full overflow-hidden">
                <div class="h-full bg-gradient-to-r from-indigo-500 to-indigo-300 w-[99.8%] rounded-full relative"></div>
              </div>
            </div>
          </div>
        </div>

        <div class="flex-1"></div>

        <div class="pt-4 border-t border-slate-100 dark:border-slate-800/80">
          <a href="tel:192" class="flex items-center gap-4 w-full p-3.5 rounded-2xl bg-gradient-to-r from-rose-500 to-red-600 hover:from-rose-600 hover:to-red-700 text-white transition-all shadow-lg shadow-rose-500/30 group relative overflow-hidden">
            <div class="absolute inset-0 bg-white/10 w-full h-full transform -skew-x-12 -translate-x-full group-hover:translate-x-full transition-transform duration-700"></div>
            <div class="w-10 h-10 rounded-xl bg-white/20 flex items-center justify-center group-hover:scale-110 transition-transform relative z-10 shadow-inner">
              <i class="fas fa-phone-volume text-white text-lg animate-pulse"></i>
            </div>
            <div class="relative z-10">
              <span class="block font-extrabold text-[14px] tracking-wide" style="font-family: 'Montserrat', sans-serif;">EMERGÊNCIA</span>
              <span class="block text-rose-100 font-semibold text-[10px] mt-0.5">Ligar para o SAMU (192)</span>
            </div>
          </a>
        </div>
      </nav>

    </div>
  </aside>
</template>

<script setup lang="ts">
import KoalaIcon from '~/components/KoalaIcon.vue';

defineProps<{ isOpen: boolean }>();
defineEmits<{ (e: 'toggle'): void }>();

const isDark = useState('isDark');
const toggleTheme = () => { isDark.value = !isDark.value; };
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Open+Sans:wght@400;500;600;700&display=swap');
.custom-scrollbar::-webkit-scrollbar { width: 4px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.2); border-radius: 10px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
</style>