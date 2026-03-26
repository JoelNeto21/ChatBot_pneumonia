<template>
  <div class="bg-white dark:bg-slate-950 font-sans text-slate-900 dark:text-slate-100 selection:bg-indigo-100 selection:text-indigo-900 antialiased">
    
    <nav class="fixed top-0 w-full z-[100] bg-white/80 dark:bg-slate-950/80 backdrop-blur-lg border-b border-slate-200 dark:border-slate-800 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center shadow-lg shadow-indigo-500/30">
            <i class="fas fa-lungs text-white text-sm"></i>
          </div>
          <span class="text-xl font-extrabold tracking-tight text-slate-900 dark:text-white">Pneumo<span class="text-indigo-600">Assist</span></span>
        </div>
        
        <div class="hidden lg:flex items-center gap-8 text-sm font-semibold text-slate-600 dark:text-slate-300">
          <a href="#tecnologia" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Tecnologia</a>
          <a href="#metodo" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Como Funciona</a>
          <a href="#equipe" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Corpo Clínico</a>
          <a href="#precos" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Planos</a>
        </div>

        <div class="flex items-center gap-4">
                   <NuxtLink to="/chatbot" class="bg-indigo-600 text-white px-6 py-2 rounded-full text-sm font-bold hover:bg-indigo-700 hover:shadow-lg hover:shadow-indigo-500/30 transition-all duration-300">
            Iniciar Consulta
          </NuxtLink>
        </div>
      </div>
    </nav>

    <header class="relative pt-40 pb-24 px-6 overflow-hidden">
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-3xl h-[500px] bg-indigo-500/10 dark:bg-indigo-500/20 blur-[120px] rounded-full pointer-events-none"></div>

      <div class="max-w-7xl mx-auto grid lg:grid-cols-2 gap-16 items-center">
        <div class="space-y-8 z-10">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-200 dark:border-emerald-500/20">
            <i class="fas fa-shield-check text-emerald-600 text-xs"></i>
            <span class="text-xs font-bold uppercase tracking-wide text-emerald-700 dark:text-emerald-400">Base Médica Rigorosamente Certificada</span>
          </div>
          <h1 class="text-5xl lg:text-6xl font-black text-slate-900 dark:text-white leading-[1.1] tracking-tight">
            Inteligência Clínica <br/>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-blue-500">Especializada em Pulmões.</span>
          </h1>
          <p class="text-lg text-slate-600 dark:text-slate-400 max-w-xl leading-relaxed">
            O PneumoAssist utiliza visão computacional avançada (Llama 3.2) para auxiliar médicos e pacientes na pré-avaliação de exames e triagem de sintomas respiratórios em segundos.
          </p>
          <div class="flex flex-col sm:flex-row gap-4">
            <NuxtLink to="/chatbot" class="px-8 py-4 bg-indigo-600 text-white text-center rounded-xl font-bold text-base hover:-translate-y-1 hover:shadow-xl hover:shadow-indigo-500/30 transition-all duration-300">
              Fazer Análise Imediata
            </NuxtLink>
            <button class="px-8 py-4 bg-white dark:bg-slate-900 text-slate-800 dark:text-white text-center rounded-xl font-bold text-base border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 transition-all duration-300 flex items-center justify-center gap-2">
              <i class="fas fa-play text-indigo-600 text-xs"></i> Ver Demonstração
            </button>
          </div>
          <div class="pt-4 flex items-center gap-4 text-sm text-slate-500 dark:text-slate-400 font-medium">
            <div class="flex -space-x-2">
              <img src="https://i.pravatar.cc/100?img=1" class="w-8 h-8 rounded-full border-2 border-white dark:border-slate-950" alt="User">
              <img src="https://i.pravatar.cc/100?img=2" class="w-8 h-8 rounded-full border-2 border-white dark:border-slate-950" alt="User">
              <img src="https://i.pravatar.cc/100?img=3" class="w-8 h-8 rounded-full border-2 border-white dark:border-slate-950" alt="User">
            </div>
            <span>Junte-se a +2.000 profissionais de saúde.</span>
          </div>
        </div>
        
        <div class="relative flex justify-center lg:justify-end z-10">
          <div class="w-full max-w-md bg-white dark:bg-slate-900 rounded-[2rem] border border-slate-200 dark:border-slate-800 p-8 shadow-2xl shadow-slate-200/50 dark:shadow-none relative">
            <div class="absolute -top-6 -left-6 bg-white dark:bg-slate-800 p-4 rounded-2xl shadow-lg border border-slate-100 dark:border-slate-700 animate-bounce-slow">
              <i class="fas fa-check-circle text-emerald-500 text-xl mb-1"></i>
              <p class="text-xs font-bold text-slate-900 dark:text-white">Análise Concluída</p>
              <p class="text-[10px] text-slate-500">0.8 segundos (Groq LPU)</p>
            </div>
            
            <img src="https://image-generator-8092.s3.amazonaws.com/generated_images/image_6.png" class="w-full aspect-square object-cover rounded-2xl shadow-inner mb-6 border border-slate-100 dark:border-slate-800" alt="Raio-x interface" />
            
            <div class="space-y-3">
              <div class="h-2 bg-slate-100 dark:bg-slate-800 rounded-full w-3/4"></div>
              <div class="h-2 bg-slate-100 dark:bg-slate-800 rounded-full w-1/2"></div>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="py-12 border-y border-slate-200 dark:border-slate-800/50 bg-slate-50 dark:bg-slate-900/20">
      <div class="max-w-7xl mx-auto px-6">
        <p class="text-center text-sm font-bold text-slate-400 uppercase tracking-widest mb-8">Processamento de Alta Performance Alimentado Por</p>
        <div class="flex flex-wrap justify-center items-center gap-12 opacity-50 hover:opacity-100 transition-opacity duration-500 grayscale hover:grayscale-0">
          <span class="font-black text-xl tracking-tighter">LLAMA 3.2 VISION</span>
          <span class="font-black text-xl tracking-tighter">GROQ <span class="text-orange-500">LPU</span></span>
          <span class="font-black text-xl tracking-tighter">NUXT.JS</span>
          <span class="font-black text-xl tracking-tighter text-cyan-500">TAILWIND</span>
        </div>
      </div>
    </div>

    <section id="tecnologia" class="py-24 px-6 relative">
      <div class="max-w-7xl mx-auto">
        <div class="text-center max-w-3xl mx-auto mb-16">
          <h2 class="text-sm font-bold text-indigo-600 uppercase tracking-widest mb-2">Tecnologia de Ponta</h2>
          <h3 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-4">Ferramentas de precisão clínica</h3>
          <p class="text-base text-slate-600 dark:text-slate-400">Nossa inteligência artificial foi treinada em milhares de radiografias e casos clínicos para atuar como o co-piloto perfeito para pneumologistas e clínicos gerais.</p>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="item in [
            { icon: 'fa-x-ray', t: 'Análise de Imagem HD', d: 'Processamento de Raio-X e Tomografias para detecção preliminar de opacidades, derrames e anomalias estruturais.' },
            { icon: 'fa-stethoscope', t: 'Triagem de Sintomas', d: 'Motor de inferência que correlaciona sintomas reportados (tosse, dispneia, febre) com prováveis quadros clínicos.' },
            { icon: 'fa-bolt', t: 'Velocidade Groq', d: 'Resultados em tempo real (sub-segundo) graças à infraestrutura LPU da Groq, ideal para ambientes de pronto-atendimento.' },
            { icon: 'fa-file-medical', t: 'Relatórios Estruturados', d: 'Geração automática de pré-laudos formatados no padrão médico para facilitar a revisão final pelo especialista.' },
            { icon: 'fa-lock', t: 'Privacidade LGPD', d: 'Anonimização automática de metadados DICOM na borda antes de qualquer processamento na nuvem.' },
            { icon: 'fa-mobile-screen', t: 'Acesso Multiplataforma', d: 'Funciona perfeitamente em desktops clínicos ou no smartphone do médico durante as rondas hospitalares.' }
          ]" :key="item.t" class="p-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
            <div class="w-12 h-12 bg-indigo-50 dark:bg-indigo-500/10 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
              <i :class="['fas text-indigo-600 dark:text-indigo-400 text-xl', item.icon]"></i>
            </div>
            <h4 class="font-bold text-lg text-slate-900 dark:text-white mb-3">{{ item.t }}</h4>
            <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">{{ item.d }}</p>
          </div>
        </div>
      </div>
    </section>

    <section id="metodo" class="py-24 px-6 bg-slate-900 dark:bg-slate-950 text-white relative overflow-hidden">
      <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-indigo-600/10 rounded-full blur-[100px] pointer-events-none"></div>

      <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center mb-20">
          <h2 class="text-sm font-bold text-indigo-400 uppercase tracking-widest mb-2">Fluxo de Trabalho</h2>
          <h3 class="text-3xl md:text-4xl font-bold mb-4">Como o PneumoAssist Atua</h3>
          <p class="text-slate-400 max-w-2xl mx-auto">Um processo desenhado para ser invisível e eficiente, integrando-se naturalmente à sua rotina clínica.</p>
        </div>

        <div class="grid md:grid-cols-4 gap-8">
          <div v-for="(step, i) in [
            { t: 'Upload Seguro', d: 'Submissão de exames de imagem (DICOM/JPEG) ou descrição em texto de sintomas do paciente.' },
            { t: 'Processamento IA', d: 'As redes neurais Llama 3.2 Vision analisam os dados usando hardware de inferência ultra-rápida.' },
            { t: 'Visão Didática', d: 'Geração de heatmaps (mapas de calor) sobre a imagem indicando as áreas de interesse clínico.' },
            { t: 'Apoio à Decisão', d: 'Emissão de um sumário executivo para suportar o diagnóstico final do médico responsável.' }
          ]" :key="i" class="relative group">
            <div class="text-6xl font-black text-slate-800 dark:text-slate-800/50 mb-6 group-hover:text-indigo-500 transition-colors duration-300">0{{ i + 1 }}</div>
            <h4 class="font-bold text-lg mb-3">{{ step.t }}</h4>
            <p class="text-slate-400 text-sm leading-relaxed">{{ step.d }}</p>
            
            <div v-if="i !== 3" class="hidden md:block absolute top-8 right-[-20%] w-[40%] h-[2px] bg-slate-800"></div>
          </div>
        </div>
      </div>
    </section>

    <section id="equipe" class="py-24 px-6 bg-slate-50 dark:bg-slate-900/30">
      <div class="max-w-7xl mx-auto">
        <div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-6">
          <div class="max-w-2xl">
            <h2 class="text-sm font-bold text-indigo-600 uppercase tracking-widest mb-2">Autoridade Médica</h2>
            <h3 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white">Conheça nosso Conselho</h3>
            <p class="text-base text-slate-600 dark:text-slate-400 mt-4">Nossa IA é supervisionada continuamente por especialistas com décadas de experiência nos maiores centros de referência do país.</p>
          </div>
          <button class="text-indigo-600 font-bold hover:underline whitespace-nowrap">Ver equipe completa &rarr;</button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          <div v-for="n in 4" :key="n" class="group bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 hover:shadow-xl transition-all duration-300">
            <div class="aspect-square bg-slate-100 dark:bg-slate-800 rounded-xl overflow-hidden mb-5 relative">
              <img :src="`https://i.pravatar.cc/400?img=${n + 10}`" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" alt="Médico especialista" />
              <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-black/60 to-transparent p-4">
                <p class="text-[10px] text-white font-bold uppercase tracking-widest">CRM-SP {{ 100000 + n * 1234 }}</p>
              </div>
            </div>
            <h4 class="text-lg font-bold text-slate-900 dark:text-white">Dr. Especialista {{ n }}</h4>
            <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Pneumologista Titular</p>
          </div>
        </div>
      </div>
    </section>

    <section id="precos" class="py-24 px-6">
      <div class="max-w-7xl mx-auto">
        <div class="text-center max-w-2xl mx-auto mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-4">Planos Transparentes</h2>
          <p class="text-base text-slate-600 dark:text-slate-400">Desde o estudante de medicina até a grande rede hospitalar. Escolha o plano ideal para a sua necessidade.</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto items-center">
          <div class="p-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl">
            <h4 class="text-sm font-bold uppercase tracking-widest text-slate-500 mb-2">Básico / Estudante</h4>
            <div class="text-4xl font-black text-slate-900 dark:text-white mb-2">Grátis</div>
            <p class="text-sm text-slate-500 mb-6">Para uso pessoal e testes.</p>
            <ul class="space-y-4 mb-8">
              <li class="text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3"><i class="fas fa-check text-indigo-500"></i> Até 5 Análises/Mês</li>
              <li class="text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3"><i class="fas fa-check text-indigo-500"></i> Chatbot Educativo</li>
              <li class="text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3"><i class="fas fa-check text-indigo-500"></i> Histórico de 24 horas</li>
            </ul>
            <button class="w-full py-3 rounded-xl border border-slate-200 dark:border-slate-700 font-bold text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 transition-all">Começar Agora</button>
          </div>

          <div class="p-8 bg-indigo-600 rounded-3xl relative transform md:-translate-y-4 shadow-2xl shadow-indigo-500/20">
            <div class="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-gradient-to-r from-orange-400 to-rose-400 text-white text-xs font-bold uppercase tracking-widest py-1 px-4 rounded-full">Mais Escolhido</div>
            <h4 class="text-sm font-bold uppercase tracking-widest text-indigo-200 mb-2">Profissional Médicos</h4>
            <div class="text-4xl font-black text-white mb-2">29€<span class="text-lg font-normal text-indigo-200">/mês</span></div>
            <p class="text-sm text-indigo-200 mb-6">Poder total para o dia a dia clínico.</p>
            <ul class="space-y-4 mb-8">
              <li class="text-sm text-white flex items-center gap-3"><i class="fas fa-check text-indigo-300"></i> Análises Ilimitadas</li>
              <li class="text-sm text-white flex items-center gap-3"><i class="fas fa-check text-indigo-300"></i> Processamento Prioritário HD</li>
              <li class="text-sm text-white flex items-center gap-3"><i class="fas fa-check text-indigo-300"></i> Exportação de Laudos em PDF</li>
              <li class="text-sm text-white flex items-center gap-3"><i class="fas fa-check text-indigo-300"></i> Suporte Prioritário</li>
            </ul>
            <button class="w-full py-3 rounded-xl bg-white text-indigo-600 font-bold text-sm hover:bg-indigo-50 transition-all">Assinar Profissional</button>
          </div>

          <div class="p-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl">
            <h4 class="text-sm font-bold uppercase tracking-widest text-slate-500 mb-2">Hospitais / Clínicas</h4>
            <div class="text-4xl font-black text-slate-900 dark:text-white mb-2">Custom</div>
            <p class="text-sm text-slate-500 mb-6">Integração completa para sua rede.</p>
            <ul class="space-y-4 mb-8">
              <li class="text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3"><i class="fas fa-check text-indigo-500"></i> Múltiplos Utilizadores</li>
              <li class="text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3"><i class="fas fa-check text-indigo-500"></i> API de Integração HIS/PACS</li>
              <li class="text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3"><i class="fas fa-check text-indigo-500"></i> Servidor Dedicado (On-premise opcional)</li>
            </ul>
            <button class="w-full py-3 rounded-xl border border-slate-200 dark:border-slate-700 font-bold text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 transition-all">Falar com Vendas</button>
          </div>
        </div>
      </div>
    </section>

    <section class="py-20 px-6">
      <div class="max-w-5xl mx-auto bg-indigo-50 dark:bg-indigo-900/20 border border-indigo-100 dark:border-indigo-800/50 rounded-[2rem] p-10 md:p-16 text-center">
        <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-6">Pronto para transformar sua rotina clínica?</h2>
        <p class="text-lg text-slate-600 dark:text-slate-400 mb-10 max-w-2xl mx-auto">Crie sua conta gratuitamente em menos de 1 minuto e faça o seu primeiro upload para ver o poder do Llama 3.2 Vision em ação.</p>
        <NuxtLink to="/chatbot" class="inline-block bg-indigo-600 text-white px-10 py-4 rounded-xl font-bold text-lg hover:bg-indigo-700 hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
          Acessar a Plataforma Agora
        </NuxtLink>
      </div>
    </section>

    <footer class="bg-slate-50 dark:bg-slate-950 border-t border-slate-200 dark:border-slate-800 py-16 px-6">
      <div class="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-12">
        <div class="col-span-2 space-y-6">
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center">
              <i class="fas fa-lungs text-white text-sm"></i>
            </div>
            <span class="font-extrabold text-xl">PneumoAssist</span>
          </div>
          <p class="text-sm text-slate-500 dark:text-slate-400 max-w-xs leading-relaxed">
            Ferramenta de apoio clínico baseada em Inteligência Artificial. Este software não substitui, sob nenhuma hipótese, o julgamento médico profissional.
          </p>
          <div class="flex gap-4">
            <a href="#" class="w-10 h-10 rounded-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 flex items-center justify-center text-slate-500 hover:text-indigo-600 transition-colors"><i class="fab fa-linkedin-in"></i></a>
            <a href="#" class="w-10 h-10 rounded-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 flex items-center justify-center text-slate-500 hover:text-indigo-600 transition-colors"><i class="fab fa-twitter"></i></a>
            <a href="#" class="w-10 h-10 rounded-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 flex items-center justify-center text-slate-500 hover:text-indigo-600 transition-colors"><i class="fab fa-github"></i></a>
          </div>
        </div>
        
        <div>
          <h4 class="text-sm font-bold text-slate-900 dark:text-white mb-6">Produto</h4>
          <ul class="space-y-4 text-sm text-slate-500 dark:text-slate-400">
            <li><a href="#" class="hover:text-indigo-600 transition-colors">Análise Vision</a></li>
            <li><a href="#" class="hover:text-indigo-600 transition-colors">Chatbot Clínico</a></li>
            <li><a href="#" class="hover:text-indigo-600 transition-colors">Preços</a></li>
            <li><a href="#" class="hover:text-indigo-600 transition-colors">Casos de Uso</a></li>
          </ul>
        </div>
        
        <div>
          <h4 class="text-sm font-bold text-slate-900 dark:text-white mb-6">Empresa</h4>
          <ul class="space-y-4 text-sm text-slate-500 dark:text-slate-400">
            <li><NuxtLink to="/sobre" class="hover:text-indigo-600 transition-colors">Sobre Nós</NuxtLink></li>
            <li><a href="#" class="hover:text-indigo-600 transition-colors">Conselho Médico</a></li>
            <li><a href="#" class="hover:text-indigo-600 transition-colors">Carreiras</a></li>
            <li><a href="#" class="hover:text-indigo-600 transition-colors">Contato</a></li>
          </ul>
        </div>
        
        <div>
          <h4 class="text-sm font-bold text-slate-900 dark:text-white mb-6">Legal & Ética</h4>
          <ul class="space-y-4 text-sm text-slate-500 dark:text-slate-400">
            <li><NuxtLink to="/privacidade" class="hover:text-indigo-600 transition-colors">Privacidade (LGPD)</NuxtLink></li>
            <li><a href="#" class="hover:text-indigo-600 transition-colors">Aviso de Isenção Médico</a></li>
            <li><a href="#" class="hover:text-indigo-600 transition-colors">Termos de Serviço</a></li>
            <li><a href="#" class="hover:text-indigo-600 transition-colors">Transparência IA</a></li>
          </ul>
        </div>
      </div>
      
      <div class="max-w-7xl mx-auto mt-16 pt-8 border-t border-slate-200 dark:border-slate-800/50 flex flex-col md:flex-row items-center justify-between gap-4">
        <p class="text-xs text-slate-500 dark:text-slate-400 font-medium">&copy; 2026 PneumoAssist Technologies. Todos os direitos reservados.</p>
        <div class="flex items-center gap-2 text-xs font-medium text-slate-500">
          Feito com <i class="fas fa-heart text-red-500"></i> em São Paulo, Brasil.
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup lang="ts">
useHead({
  title: 'PneumoAssist | IA Clínica Especializada em Pulmões',
  meta: [
    { name: 'description', content: 'Assistente clínico de visão computacional para triagem e análise de exames respiratórios com Llama 3.2 Vision e Groq.' }
  ],
  link: [
    { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' }
  ]
})
</script>

<style>
html { scroll-behavior: smooth; }
body { -webkit-font-smoothing: antialiased; }
.animate-bounce-slow {
  animation: bounce 3s infinite;
}
@keyframes bounce {
  0%, 100% { transform: translateY(-5%); animation-timing-function: cubic-bezier(0.8,0,1,1); }
  50% { transform: none; animation-timing-function: cubic-bezier(0,0,0.2,1); }
}
</style>