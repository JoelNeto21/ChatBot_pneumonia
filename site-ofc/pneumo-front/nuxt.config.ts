export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss'],
  
  css: ['~/assets/css/main.css'],
  
  app: {
    // AQUI: Configuração do Head para incluir o Favicon
    head: {
      title: 'PneumoAssist',
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }
      ]
    },
    // Mantém a tua configuração de animações
    pageTransition: { name: 'page', mode: 'out-in' }
  },
  
  devtools: { enabled: true },
  compatibilityDate: '2025-07-15'
})