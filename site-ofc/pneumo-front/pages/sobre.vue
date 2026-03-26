<template>
  <div class="bg-white dark:bg-slate-950 font-sans text-slate-900 dark:text-slate-100 antialiased selection:bg-indigo-100 selection:text-indigo-900 min-h-screen flex flex-col">
    
    <nav class="fixed top-0 w-full z-[100] bg-white/80 dark:bg-slate-950/80 backdrop-blur-lg border-b border-slate-200 dark:border-slate-800 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
        <NuxtLink to="/" class="flex items-center gap-3">
          <div class="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center shadow-lg shadow-indigo-500/30">
            <i class="fas fa-lungs text-white text-sm"></i>
          </div>
          <span class="text-xl font-extrabold tracking-tight text-slate-900 dark:text-white">Pneumo<span class="text-indigo-600">Assist</span></span>
        </NuxtLink>
        <div class="flex items-center gap-4">
          <NuxtLink to="/" class="text-sm font-bold text-slate-600 dark:text-slate-300 hover:text-indigo-600 transition-colors">Voltar ao Início</NuxtLink>
          <NuxtLink to="/chatbot" class="bg-indigo-600 text-white px-5 py-2 rounded-full text-sm font-bold hover:bg-indigo-700 transition-all duration-300">
            Aceder à Plataforma
          </NuxtLink>
        </div>
      </div>
    </nav>

    <header class="relative pt-40 pb-20 px-6 overflow-hidden bg-slate-50 dark:bg-slate-900/30">
      <div class="absolute top-0 right-0 w-1/2 h-full bg-indigo-50 dark:bg-indigo-900/10 clip-path-slant pointer-events-none"></div>
      
      <div class="max-w-4xl mx-auto text-center relative z-10">
        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-indigo-100 dark:bg-indigo-900/30 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest mb-6">
          A Nossa História & Missão
        </div>
        <h1 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white mb-6 tracking-tight leading-tight">
          Unimos a precisão médica à <br class="hidden md:block" />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-blue-500">Inteligência Artificial de Ponta.</span>
        </h1>
        <p class="text-lg text-slate-600 dark:text-slate-400 leading-relaxed max-w-2xl mx-auto">
          O PneumoAssist nasceu da necessidade de democratizar o acesso a triagens respiratórias rápidas e precisas. Somos uma equipa multidisciplinar de médicos especialistas e engenheiros de IA dedicados a salvar vidas através da tecnologia.
        </p>
      </div>
    </header>

    <section class="py-20 px-6 bg-white dark:bg-slate-950">
      <div class="max-w-7xl mx-auto">
        <div class="grid md:grid-cols-3 gap-10">
          <div class="space-y-4">
            <div class="w-12 h-12 bg-emerald-50 dark:bg-emerald-500/10 rounded-2xl flex items-center justify-center">
              <i class="fas fa-user-md text-emerald-600 dark:text-emerald-400 text-xl"></i>
            </div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white">Apoio, não Substituição</h3>
            <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
              A nossa IA (Llama 3.2 Vision) foi desenhada para ser um "co-piloto" do médico. Acreditamos que a decisão final e o lado humano do cuidado pertencerão sempre ao profissional de saúde.
            </p>
          </div>
          <div class="space-y-4">
            <div class="w-12 h-12 bg-indigo-50 dark:bg-indigo-500/10 rounded-2xl flex items-center justify-center">
              <i class="fas fa-shield-halved text-indigo-600 dark:text-indigo-400 text-xl"></i>
            </div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white">Privacidade e LGPD</h3>
            <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
              Tratamos dados sensíveis com rigor militar. As imagens submetidas são automaticamente anonimizadas na origem e não são utilizadas para treinar modelos de terceiros sem consentimento.
            </p>
          </div>
          <div class="space-y-4">
            <div class="w-12 h-12 bg-blue-50 dark:bg-blue-500/10 rounded-2xl flex items-center justify-center">
              <i class="fas fa-microscope text-blue-600 dark:text-blue-400 text-xl"></i>
            </div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white">Validação Científica</h3>
            <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
              Os nossos algoritmos são continuamente testados contra bases de dados clínicas certificadas e validados por um conselho médico independente para garantir baixíssimos níveis de falsos positivos.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 bg-slate-50 dark:bg-slate-900/20 border-y border-slate-100 dark:border-slate-800">
      <div class="max-w-7xl mx-auto">
        <div class="text-center max-w-3xl mx-auto mb-16">
          <h2 class="text-sm font-bold text-indigo-600 uppercase tracking-widest mb-2">Quem treina a nossa IA</h2>
          <h3 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-4">Conselho Médico Fundador</h3>
          <p class="text-base text-slate-600 dark:text-slate-400">Profissionais com décadas de experiência nas melhores instituições, responsáveis pela curadoria de dados e auditoria contínua dos diagnósticos da IA.</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div class="bg-white dark:bg-slate-900 rounded-3xl p-6 border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-xl transition-all duration-300 group">
            <div class="flex gap-5 items-start mb-6">
              <div class="w-24 h-24 rounded-2xl overflow-hidden shrink-0 relative">
                <img src="https://i.pravatar.cc/300?img=32" alt="Dra. Mariana Costa" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                <div class="absolute inset-0 border border-black/10 rounded-2xl"></div>
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-900 dark:text-white">Dra. Mariana Costa</h4>
                <p class="text-xs text-indigo-600 dark:text-indigo-400 font-bold uppercase tracking-wide mt-1 mb-2">Pneumologista Chefe</p>
                <span class="inline-block bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-[10px] px-2 py-1 rounded font-bold">CRM 123456</span>
              </div>
            </div>
            <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed mb-4">
              Doutorada em Medicina Pulmonar. Com mais de 15 anos de experiência clínica, lidera a validação dos modelos de triagem e a calibração de falsos negativos da plataforma.
            </p>
            <div class="flex gap-3 pt-4 border-t border-slate-100 dark:border-slate-800">
              <a href="#" class="text-slate-400 hover:text-indigo-600 transition-colors"><i class="fab fa-linkedin text-lg"></i></a>
              <a href="#" class="text-slate-400 hover:text-indigo-600 transition-colors"><i class="fas fa-envelope text-lg"></i></a>
            </div>
          </div>

          <div class="bg-white dark:bg-slate-900 rounded-3xl p-6 border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-xl transition-all duration-300 group">
            <div class="flex gap-5 items-start mb-6">
              <div class="w-24 h-24 rounded-2xl overflow-hidden shrink-0 relative">
                <img src="https://i.pravatar.cc/300?img=11" alt="Dr. Ricardo Alves" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                <div class="absolute inset-0 border border-black/10 rounded-2xl"></div>
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-900 dark:text-white">Dr. Ricardo Alves</h4>
                <p class="text-xs text-indigo-600 dark:text-indigo-400 font-bold uppercase tracking-wide mt-1 mb-2">Radiologista Torácico</p>
                <span class="inline-block bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-[10px] px-2 py-1 rounded font-bold">CRM 654321</span>
              </div>
            </div>
            <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed mb-4">
              Especialista na interpretação de imagem avançada. É o responsável por afinar a precisão do Llama 3.2 Vision na identificação de micro-opacidades em Raio-X.
            </p>
            <div class="flex gap-3 pt-4 border-t border-slate-100 dark:border-slate-800">
              <a href="#" class="text-slate-400 hover:text-indigo-600 transition-colors"><i class="fab fa-linkedin text-lg"></i></a>
            </div>
          </div>

          <div class="bg-white dark:bg-slate-900 rounded-3xl p-6 border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-xl transition-all duration-300 group">
            <div class="flex gap-5 items-start mb-6">
              <div class="w-24 h-24 rounded-2xl overflow-hidden shrink-0 relative">
                <img src="https://i.pravatar.cc/300?img=53" alt="Eng. Bruno Silva" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                <div class="absolute inset-0 border border-black/10 rounded-2xl"></div>
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-900 dark:text-white">Eng. Bruno Silva</h4>
                <p class="text-xs text-emerald-600 dark:text-emerald-400 font-bold uppercase tracking-wide mt-1 mb-2">CTO & Head de IA</p>
                <span class="inline-block bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 text-[10px] px-2 py-1 rounded font-bold">Tech Lead</span>
              </div>
            </div>
            <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed mb-4">
              Arquiteto de infraestrutura responsável pela implementação da inferência ultra-rápida via Groq LPU e garantia da encriptação end-to-end dos dados dos pacientes.
            </p>
            <div class="flex gap-3 pt-4 border-t border-slate-100 dark:border-slate-800">
              <a href="#" class="text-slate-400 hover:text-indigo-600 transition-colors"><i class="fab fa-linkedin text-lg"></i></a>
              <a href="#" class="text-slate-400 hover:text-indigo-600 transition-colors"><i class="fab fa-github text-lg"></i></a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 flex-grow">
      <div class="max-w-4xl mx-auto bg-indigo-600 rounded-[2.5rem] p-10 md:p-16 text-center relative overflow-hidden shadow-2xl shadow-indigo-600/30">
        <div class="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full blur-3xl"></div>
        <div class="absolute bottom-0 left-0 w-64 h-64 bg-black/10 rounded-full blur-3xl"></div>
        
        <h2 class="text-3xl md:text-4xl font-bold text-white mb-6 relative z-10">Faça parte do futuro da medicina respiratória</h2>
        <p class="text-indigo-100 mb-10 text-lg max-w-2xl mx-auto relative z-10">
          Seja você um paciente à procura de uma segunda opinião rápida, ou uma clínica que deseja otimizar o fluxo de triagem, a nossa equipa está pronta para ajudar.
        </p>
        <div class="flex flex-col sm:flex-row justify-center gap-4 relative z-10">
          <NuxtLink to="/chatbot" class="bg-white text-indigo-600 px-8 py-4 rounded-xl font-bold text-base hover:bg-slate-50 hover:shadow-lg transition-all">
            Testar a Inteligência Artificial
          </NuxtLink>
          <a href="mailto:contato@pneumoassist.com" class="bg-indigo-700/50 text-white border border-indigo-500/50 px-8 py-4 rounded-xl font-bold text-base hover:bg-indigo-700 transition-all flex items-center justify-center gap-2">
            <i class="fas fa-envelope text-sm"></i> Contactar Equipa Comercial
          </a>
        </div>
      </div>
    </section>

    <footer class="py-8 text-center border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-950">
      <p class="text-xs text-slate-500 font-medium">
        &copy; 2026 PneumoAssist. Feito com <i class="fas fa-heart text-red-500 mx-1"></i> pela nossa equipa para a saúde global.
      </p>
    </footer>

  </div>
</template>

<script setup lang="ts">
useHead({
  title: 'Sobre Nós | PneumoAssist',
  meta: [
    { name: 'description', content: 'Conheça o conselho médico e a equipa de engenharia de IA por trás do PneumoAssist.' }
  ],
  link: [
    { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' }
  ]
})
</script>

<style scoped>
.clip-path-slant {
  clip-path: polygon(20% 0, 100% 0, 100% 100%, 0% 100%);
}
</style>