<template>
  <div class="bg-white dark:bg-slate-950 font-sans text-slate-900 dark:text-slate-100 selection:bg-indigo-100 selection:text-indigo-900 antialiased overflow-x-hidden">
    
    <nav 
      :class="[
        'fixed top-0 w-full z-[100] backdrop-blur-lg border-b transition-all duration-500',
        showNavbar ? 'translate-y-0 bg-white/80 dark:bg-slate-950/80 border-slate-200 dark:border-slate-800' : '-translate-y-full opacity-0'
      ]"
    >
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
          <a href="#mascote" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Mascote</a>
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

      <div class="max-w-7xl mx-auto grid lg:grid-cols-2 gap-16 items-center fade-in-up">
        <div class="space-y-8 z-10">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-200 dark:border-emerald-500/20 animate-pulse-slow">
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
            <button class="px-8 py-4 bg-white dark:bg-slate-900 text-slate-800 dark:text-white text-center rounded-xl font-bold text-base border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 transition-all duration-300 flex items-center justify-center gap-2 group">
              <i class="fas fa-play text-indigo-600 text-xs group-hover:scale-125 transition-transform"></i> Ver Demonstração
            </button>
          </div>
          <div class="pt-4 flex items-center gap-4 text-sm text-slate-500 dark:text-slate-400 font-medium">
            <div class="flex -space-x-2">
              <img src="https://i.pravatar.cc/100?img=1" class="w-8 h-8 rounded-full border-2 border-white dark:border-slate-950 hover:z-10 transition-transform hover:scale-110" alt="User">
              <img src="https://i.pravatar.cc/100?img=2" class="w-8 h-8 rounded-full border-2 border-white dark:border-slate-950 hover:z-10 transition-transform hover:scale-110" alt="User">
              <img src="https://i.pravatar.cc/100?img=3" class="w-8 h-8 rounded-full border-2 border-white dark:border-slate-950 hover:z-10 transition-transform hover:scale-110" alt="User">
            </div>
            <span>Junte-se a +2.000 profissionais de saúde.</span>
          </div>
        </div>
        
        <div class="relative flex justify-center lg:justify-end z-10">
          <div class="w-full max-w-md bg-white dark:bg-slate-900 rounded-[2rem] border border-slate-200 dark:border-slate-800 p-8 shadow-2xl shadow-slate-200/50 dark:shadow-none relative hover:shadow-indigo-500/20 transition-shadow duration-500">
            <div class="absolute -top-6 -left-6 bg-white dark:bg-slate-800 p-4 rounded-2xl shadow-lg border border-slate-100 dark:border-slate-700 animate-float">
              <i class="fas fa-check-circle text-emerald-500 text-xl mb-1"></i>
              <p class="text-xs font-bold text-slate-900 dark:text-white">Análise Concluída</p>
              <p class="text-[10px] text-slate-500">0.8 segundos (Groq LPU)</p>
            </div>
            
            <img src="https://image-generator-8092.s3.amazonaws.com/generated_images/image_6.png" class="w-full aspect-square object-cover rounded-2xl shadow-inner mb-6 border border-slate-100 dark:border-slate-800" alt="Raio-x interface" />
            
            <div class="space-y-3">
              <div class="h-2 bg-slate-100 dark:bg-slate-800 rounded-full w-3/4 overflow-hidden">
                <div class="h-full bg-indigo-500 w-full animate-progress"></div>
              </div>
              <div class="h-2 bg-slate-100 dark:bg-slate-800 rounded-full w-1/2"></div>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="py-12 border-y border-slate-200 dark:border-slate-800/50 bg-slate-50 dark:bg-slate-900/20">
      <div class="max-w-7xl mx-auto px-6">
        <p class="text-center text-sm font-bold text-slate-400 uppercase tracking-widest mb-8">Processamento de Alta Performance Alimentado Por</p>
        <div class="flex flex-wrap justify-center items-center gap-12 opacity-60 hover:opacity-100 transition-opacity duration-500 grayscale hover:grayscale-0">
          <span class="font-black text-xl tracking-tighter hover:text-blue-600 transition-colors cursor-default">LLAMA 3.2 VISION</span>
          <span class="font-black text-xl tracking-tighter hover:text-orange-500 transition-colors cursor-default">GROQ <span class="text-orange-500">LPU</span></span>
          <span class="font-black text-xl tracking-tighter hover:text-green-500 transition-colors cursor-default">NUXT.JS</span>
          <span class="font-black text-xl tracking-tighter hover:text-cyan-500 transition-colors cursor-default">TAILWIND</span>
        </div>
      </div>
    </div>

    <section id="tecnologia" class="py-24 px-6 relative">
      <div class="max-w-7xl mx-auto">
        <div class="text-center max-w-3xl mx-auto mb-16 fade-in-up">
          <h2 class="text-sm font-bold text-indigo-600 uppercase tracking-widest mb-2">Tecnologia de Ponta</h2>
          <h3 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-4">Ferramentas de precisão clínica</h3>
          <p class="text-base text-slate-600 dark:text-slate-400">Nossa inteligência artificial foi treinada em milhares de radiografias e casos clínicos para atuar como o co-piloto perfeito para pneumologistas e clínicos gerais.</p>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 stagger-children">
          <div v-for="item in [
            { icon: 'fa-x-ray', t: 'Análise de Imagem HD', d: 'Processamento de Raio-X e Tomografias para detecção preliminar de opacidades, derrames e anomalias estruturais.' },
            { icon: 'fa-stethoscope', t: 'Triagem de Sintomas', d: 'Motor de inferência que correlaciona sintomas reportados com prováveis quadros clínicos.' },
            { icon: 'fa-bolt', t: 'Velocidade Groq', d: 'Resultados em tempo real graças à infraestrutura LPU da Groq, ideal para pronto-atendimento.' },
            { icon: 'fa-file-medical', t: 'Relatórios Estruturados', d: 'Geração automática de pré-laudos formatados no padrão médico para facilitar a revisão.' },
            { icon: 'fa-lock', t: 'Privacidade LGPD', d: 'Anonimização automática de metadados DICOM na borda antes de qualquer processamento.' },
            { icon: 'fa-mobile-screen', t: 'Acesso Multiplataforma', d: 'Funciona perfeitamente em desktops clínicos ou no smartphone do médico nas rondas.' }
          ]" :key="item.t" class="p-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl hover:shadow-2xl hover:shadow-indigo-500/10 hover:-translate-y-2 transition-all duration-300 group cursor-pointer">
            <div class="w-12 h-12 bg-indigo-50 dark:bg-indigo-500/10 rounded-xl flex items-center justify-center mb-6 group-hover:bg-indigo-600 group-hover:text-white transition-colors duration-300">
              <i :class="['fas text-indigo-600 dark:text-indigo-400 group-hover:text-white text-xl transition-colors', item.icon]"></i>
            </div>
            <h4 class="font-bold text-lg text-slate-900 dark:text-white mb-3">{{ item.t }}</h4>
            <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">{{ item.d }}</p>
          </div>
        </div>
      </div>
    </section>

    <section id="mascote" class="py-20 px-6 bg-gradient-to-b from-slate-50 to-white dark:from-slate-900/50 dark:to-slate-950 border-y border-slate-200 dark:border-slate-800">
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center gap-12">
        <div class="flex-1 text-center md:text-left space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-100 dark:bg-indigo-900/30 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest">
            <i class="fas fa-robot"></i> Seu Novo Assistente
          </div>
          <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white">
            Conheça o <span class="text-indigo-600">Pneumito</span>
          </h2>
          <p class="text-lg text-slate-600 dark:text-slate-400">
            A tecnologia não precisa ser fria. Nosso mascote representa a união entre o acolhimento humano e a precisão da inteligência artificial. Ele vai guiar seus pacientes na triagem e ajudar você na análise dos laudos.
          </p>
          <ul class="space-y-3 text-left max-w-md mx-auto md:mx-0">
            <li class="flex items-center gap-3 text-slate-700 dark:text-slate-300">
              <i class="fas fa-check-circle text-emerald-500"></i> Amigável para pacientes de todas as idades
            </li>
            <li class="flex items-center gap-3 text-slate-700 dark:text-slate-300">
              <i class="fas fa-check-circle text-emerald-500"></i> Respostas claras e humanizadas
            </li>
          </ul>
        </div>
        <div class="flex-1 relative flex justify-center">
          <div class="absolute inset-0 bg-indigo-400/20 blur-3xl rounded-full"></div>
          <div class="relative z-10 w-64 h-64 md:w-80 md:h-80 bg-slate-200 dark:bg-slate-800 rounded-[3rem] border-4 border-white dark:border-slate-700 shadow-2xl flex items-center justify-center overflow-hidden animate-float">
            <img src="https://placehold.co/400x400/e2e8f0/475569?text=Mascote+Aqui" alt="Mascote Pneumito" class="w-full h-full object-cover" />
          </div>
        </div>
      </div>
    </section>

    <section id="metodo" class="py-24 px-6 bg-slate-900 dark:bg-slate-950 text-white relative overflow-hidden">
      <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-indigo-600/10 rounded-full blur-[100px] pointer-events-none"></div>

      <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center mb-20 fade-in-up">
          <h2 class="text-sm font-bold text-indigo-400 uppercase tracking-widest mb-2">Fluxo de Trabalho</h2>
          <h3 class="text-3xl md:text-4xl font-bold mb-4">Como o PneumoAssist Atua</h3>
          <p class="text-slate-400 max-w-2xl mx-auto">Um processo desenhado para ser invisível e eficiente, integrando-se naturalmente à sua rotina clínica.</p>
        </div>

        <div class="grid md:grid-cols-4 gap-8">
          <div v-for="(step, i) in [
            { t: 'Upload Seguro', d: 'Submissão de exames de imagem ou descrição em texto de sintomas do paciente.' },
            { t: 'Processamento IA', d: 'As redes neurais analisam os dados usando hardware de inferência ultra-rápida.' },
            { t: 'Visão Didática', d: 'Geração de heatmaps sobre a imagem indicando áreas de interesse clínico.' },
            { t: 'Apoio à Decisão', d: 'Emissão de um sumário executivo para suportar o diagnóstico final do médico.' }
          ]" :key="i" class="relative group">
            <div class="text-6xl font-black text-slate-800 dark:text-slate-800/50 mb-6 group-hover:text-indigo-500 group-hover:-translate-y-2 transition-all duration-300">0{{ i + 1 }}</div>
            <h4 class="font-bold text-lg mb-3">{{ step.t }}</h4>
            <p class="text-slate-400 text-sm leading-relaxed">{{ step.d }}</p>
            
            <div v-if="i !== 3" class="hidden md:block absolute top-8 right-[-20%] w-[40%] h-[2px] bg-slate-800 overflow-hidden">
              <div class="w-full h-full bg-indigo-500 -translate-x-full group-hover:animate-slide-right"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 bg-slate-50 dark:bg-slate-900/30">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16 fade-in-up">
          <h2 class="text-sm font-bold text-indigo-600 uppercase tracking-widest mb-2">Casos de Sucesso</h2>
          <h3 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white">Quem usa, confia.</h3>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
          <div v-for="n in 3" :key="n" class="bg-white dark:bg-slate-900 p-8 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-xl transition-shadow">
            <div class="flex text-yellow-400 text-sm mb-4">
              <i class="fas fa-star" v-for="s in 5" :key="s"></i>
            </div>
            <p class="text-slate-600 dark:text-slate-400 mb-6 italic">"A integração do PneumoAssist no plantão reduziu nosso tempo de triagem de imagens em quase 40%. A assertividade da marcação de anomalias é impressionante."</p>
            <div class="flex items-center gap-4">
              <img :src="`https://i.pravatar.cc/100?img=${n+20}`" class="w-12 h-12 rounded-full" alt="Avatar">
              <div>
                <h4 class="font-bold text-slate-900 dark:text-white text-sm">Dr. Carlos Silva</h4>
                <p class="text-xs text-slate-500">Diretor Clínico, Hospital São Paulo</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="precos" class="py-24 px-6 relative z-10">
      <div class="max-w-7xl mx-auto">
        <div class="text-center max-w-2xl mx-auto mb-16 fade-in-up">
          <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-4">Planos Transparentes</h2>
          <p class="text-base text-slate-600 dark:text-slate-400">Desde o estudante de medicina até a grande rede hospitalar. Escolha o plano ideal para a sua necessidade.</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto items-center">
          <div class="p-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl hover:border-indigo-500/50 transition-colors">
            <h4 class="text-sm font-bold uppercase tracking-widest text-slate-500 mb-2">Básico / Estudante</h4>
            <div class="text-4xl font-black text-slate-900 dark:text-white mb-2">Grátis</div>
            <p class="text-sm text-slate-500 mb-6">Para uso pessoal e testes.</p>
            <ul class="space-y-4 mb-8">
              <li class="text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3"><i class="fas fa-check text-indigo-500"></i> Até 5 Análises/Mês</li>
              <li class="text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3"><i class="fas fa-check text-indigo-500"></i> Chatbot Educativo</li>
            </ul>
            <button class="w-full py-3 rounded-xl border border-slate-200 dark:border-slate-700 font-bold text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 transition-all">Começar Agora</button>
          </div>

          <div class="p-8 bg-indigo-600 rounded-3xl relative transform md:-translate-y-4 shadow-2xl shadow-indigo-500/30 border border-indigo-500">
            <div class="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-gradient-to-r from-orange-400 to-rose-400 text-white text-xs font-bold uppercase tracking-widest py-1 px-4 rounded-full shadow-lg">Mais Escolhido</div>
            <h4 class="text-sm font-bold uppercase tracking-widest text-indigo-200 mb-2">Profissional</h4>
            <div class="text-4xl font-black text-white mb-2">29€<span class="text-lg font-normal text-indigo-200">/mês</span></div>
            <p class="text-sm text-indigo-200 mb-6">Poder total para o dia a dia clínico.</p>
            <ul class="space-y-4 mb-8">
              <li class="text-sm text-white flex items-center gap-3"><i class="fas fa-check text-indigo-300"></i> Análises Ilimitadas</li>
              <li class="text-sm text-white flex items-center gap-3"><i class="fas fa-check text-indigo-300"></i> Exportação em PDF</li>
              <li class="text-sm text-white flex items-center gap-3"><i class="fas fa-check text-indigo-300"></i> Suporte Prioritário</li>
            </ul>
            <button class="w-full py-3 rounded-xl bg-white text-indigo-600 font-bold text-sm hover:bg-indigo-50 hover:scale-[1.02] transition-all">Assinar Profissional</button>
          </div>

          <div class="p-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl hover:border-indigo-500/50 transition-colors">
            <h4 class="text-sm font-bold uppercase tracking-widest text-slate-500 mb-2">Hospitais</h4>
            <div class="text-4xl font-black text-slate-900 dark:text-white mb-2">Custom</div>
            <p class="text-sm text-slate-500 mb-6">Integração completa para sua rede.</p>
            <ul class="space-y-4 mb-8">
              <li class="text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3"><i class="fas fa-check text-indigo-500"></i> Múltiplos Utilizadores</li>
              <li class="text-sm text-slate-600 dark:text-slate-400 flex items-center gap-3"><i class="fas fa-check text-indigo-500"></i> API de Integração PACS</li>
            </ul>
            <button class="w-full py-3 rounded-xl border border-slate-200 dark:border-slate-700 font-bold text-sm text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 transition-all">Falar com Vendas</button>
          </div>
        </div>
      </div>
    </section>

    <section class="py-20 px-6 max-w-4xl mx-auto">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-slate-900 dark:text-white">Dúvidas Frequentes</h2>
      </div>
      <div class="space-y-4">
        <details class="group bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl [&_summary::-webkit-details-marker]:hidden">
          <summary class="flex items-center justify-between p-6 cursor-pointer font-bold text-slate-900 dark:text-white">
            A IA substitui o diagnóstico médico?
            <span class="transition group-open:rotate-180"><i class="fas fa-chevron-down text-indigo-500"></i></span>
          </summary>
          <div class="px-6 pb-6 text-slate-600 dark:text-slate-400 text-sm">
            Não. O PneumoAssist é classificado como um Sistema de Apoio à Decisão Clínica (CDSS). Ele atua como um "co-piloto" para destacar áreas de interesse e agilizar o processo, mas o laudo e diagnóstico final são de responsabilidade exclusiva do médico.
          </div>
        </details>
        <details class="group bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl [&_summary::-webkit-details-marker]:hidden">
          <summary class="flex items-center justify-between p-6 cursor-pointer font-bold text-slate-900 dark:text-white">
            Meus dados ou de meus pacientes estão seguros?
            <span class="transition group-open:rotate-180"><i class="fas fa-chevron-down text-indigo-500"></i></span>
          </summary>
          <div class="px-6 pb-6 text-slate-600 dark:text-slate-400 text-sm">
            Sim. Somos rigorosamente adequados à LGPD e HIPAA. Todas as imagens processadas têm seus metadados (identificação do paciente) removidos localmente antes de serem enviadas para inferência na nuvem.
          </div>
        </details>
      </div>
    </section>

    <section class="py-20 px-6">
      <div class="max-w-5xl mx-auto bg-gradient-to-br from-indigo-50 to-blue-50 dark:from-indigo-900/40 dark:to-blue-900/20 border border-indigo-100 dark:border-indigo-800/50 rounded-[2rem] p-10 md:p-16 text-center shadow-xl shadow-indigo-500/5 relative overflow-hidden">
        <div class="absolute top-0 right-0 p-8 opacity-10 pointer-events-none"><i class="fas fa-lungs text-9xl"></i></div>
        <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-6 relative z-10">Pronto para transformar sua rotina clínica?</h2>
        <p class="text-lg text-slate-600 dark:text-slate-400 mb-10 max-w-2xl mx-auto relative z-10">Crie sua conta gratuitamente em menos de 1 minuto e faça o seu primeiro upload para ver o poder do Llama 3.2 Vision em ação.</p>
        <NuxtLink to="/chatbot" class="relative z-10 inline-block bg-indigo-600 text-white px-10 py-4 rounded-xl font-bold text-lg hover:bg-indigo-700 hover:shadow-2xl hover:shadow-indigo-500/40 hover:-translate-y-1 transition-all duration-300">
          Acessar a Plataforma Agora
        </NuxtLink>
      </div>
    </section>

    <footer ref="footerElement" class="bg-slate-900 dark:bg-slate-950 text-slate-300 py-20 px-6 border-t border-slate-800">
      <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12">
        <div class="col-span-1 lg:col-span-2 space-y-6">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-indigo-600 rounded-lg flex items-center justify-center">
              <i class="fas fa-lungs text-white text-lg"></i>
            </div>
            <span class="font-extrabold text-2xl text-white">Pneumo<span class="text-indigo-500">Assist</span></span>
          </div>
          <p class="text-sm text-slate-400 max-w-sm leading-relaxed">
            Ferramenta de apoio clínico baseada em Inteligência Artificial para análise avançada de imagem e triagem pulmonar.
          </p>
          
          <div class="pt-4">
            <p class="text-xs font-bold uppercase tracking-widest text-slate-500 mb-3">Inscreva-se na Newsletter Científica</p>
            <div class="flex gap-2 max-w-sm">
              <input type="email" placeholder="seu@email.com" class="bg-slate-800 border border-slate-700 rounded-lg px-4 py-2 text-sm w-full focus:outline-none focus:border-indigo-500 transition-colors text-white">
              <button class="bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-2 rounded-lg text-sm font-bold transition-colors">Assinar</button>
            </div>
          </div>
        </div>
        
        <div>
          <h4 class="text-sm font-bold text-white mb-6">Produto</h4>
          <ul class="space-y-4 text-sm text-slate-400">
            <li><NuxtLink to="/chatbot" class="hover:text-indigo-400 transition-colors">Plataforma Vision</NuxtLink></li>
            <li><a href="#metodo" class="hover:text-indigo-400 transition-colors">Como Funciona</a></li>
            <li><a href="#precos" class="hover:text-indigo-400 transition-colors">Preços</a></li>
          </ul>
        </div>
        
        <div>
          <h4 class="text-sm font-bold text-white mb-6">Empresa</h4>
          <ul class="space-y-4 text-sm text-slate-400">
            <li><NuxtLink to="/sobre" class="hover:text-indigo-400 transition-colors text-indigo-400 font-medium">Sobre Nós (Equipe)</NuxtLink></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Contato</a></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Blog Médico</a></li>
          </ul>
        </div>
        
        <div>
          <h4 class="text-sm font-bold text-white mb-6">Legal</h4>
          <ul class="space-y-4 text-sm text-slate-400">
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Política de Privacidade</a></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Termos de Uso</a></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Aviso Médico</a></li>
          </ul>
          
          <div class="flex gap-4 mt-8">
            <a href="#" class="text-slate-400 hover:text-white transition-colors"><i class="fab fa-linkedin text-xl"></i></a>
            <a href="#" class="text-slate-400 hover:text-white transition-colors"><i class="fab fa-twitter text-xl"></i></a>
            <a href="#" class="text-slate-400 hover:text-white transition-colors"><i class="fab fa-instagram text-xl"></i></a>
          </div>
        </div>
      </div>
      
      <div class="max-w-7xl mx-auto mt-16 pt-8 border-t border-slate-800 flex flex-col md:flex-row items-center justify-between gap-4">
        <p class="text-xs text-slate-500 font-medium">&copy; {{ new Date().getFullYear() }} PneumoAssist Technologies. Todos os direitos reservados.</p>
        <div class="flex items-center gap-2 text-xs font-medium text-slate-500">
          Feito com <i class="fas fa-heart text-rose-500"></i> no Brasil.
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

// SEO e Meta Tags
useHead({
  title: 'PneumoAssist | IA Clínica Especializada em Pulmões',
  meta: [
    { name: 'description', content: 'Assistente clínico de visão computacional para triagem e análise de exames respiratórios com Llama 3.2 Vision e Groq.' }
  ],
  link: [
    { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' }
  ]
})

// Lógica para esconder Navbar no Footer
const footerElement = ref(null)
const showNavbar = ref(true)
let observer: IntersectionObserver | null = null

onMounted(() => {
  observer = new IntersectionObserver((entries) => {
    // Se o rodapé estiver visível na tela, esconde a navbar. Caso contrário, mostra.
    entries.forEach(entry => {
      showNavbar.value = !entry.isIntersecting
    })
  }, { 
    threshold: 0.1 // Dispara quando 10% do rodapé aparecer
  })

  if (footerElement.value) {
    observer.observe(footerElement.value)
  }
})

onUnmounted(() => {
  if (observer) observer.disconnect()
})
</script>

<style>
/* Base Setup */
html { scroll-behavior: smooth; }
body { -webkit-font-smoothing: antialiased; }

/* Animações Nativas Adicionadas */
.animate-float {
  animation: float 6s ease-in-out infinite;
}
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
  100% { transform: translateY(0px); }
}

.animate-pulse-slow {
  animation: pulse-slow 4s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
@keyframes pulse-slow {
  0%, 100% { opacity: 1; }
  50% { opacity: .7; }
}

.animate-progress {
  animation: loadProgress 2s ease-out forwards;
}
@keyframes loadProgress {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(0); }
}

.animate-slide-right {
  animation: slideRight 1s ease-out forwards;
}
@keyframes slideRight {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(0); }
}

/* Utilitário para fade in simples nos elementos */
.fade-in-up {
  animation: fadeInUp 1s ease-out;
}
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}
</style>