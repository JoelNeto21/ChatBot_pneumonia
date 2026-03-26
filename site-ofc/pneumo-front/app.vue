<template>
  <div :class="{ 'dark': isDark }">
    <div class="min-h-screen flex flex-col w-full bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 font-sans transition-colors duration-500 overflow-x-hidden">
      <NuxtPage />
    </div>
  </div>
</template>

<script setup lang="ts">
// Estado global para o Dark Mode
const isDark = useState('isDark', () => false);

// Injetar FontAwesome e configurar os títulos das abas de forma inteligente
useHead({
  titleTemplate: (titleChunk) => {
    // Se a página tiver título, junta com PneumoAssist. Se não, mostra o padrão.
    return titleChunk ? `${titleChunk} - PneumoAssist` : 'PneumoAssist - IA Respiratória';
  },
  link: [
    { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' }
  ]
});
</script>

<style>
/* 1. Transição Suave e Moderna entre Páginas (ex: do Index para o Chatbot) */
.page-enter-active,
.page-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  transform: translateY(15px);
  filter: blur(4px);
}

/* 2. Barra de Rolagem (Scrollbar) Premium estilo macOS */
::-webkit-scrollbar {
  width: 8px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: rgba(148, 163, 184, 0.4);
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: rgba(148, 163, 184, 0.7);
}

/* Scrollbar no Dark Mode */
.dark ::-webkit-scrollbar-thumb {
  background: rgba(71, 85, 105, 0.5);
}
.dark ::-webkit-scrollbar-thumb:hover {
  background: rgba(71, 85, 105, 0.9);
}

/* 3. Scroll Suave global */
html {
  scroll-behavior: smooth;
}
</style>