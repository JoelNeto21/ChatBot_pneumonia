<template>
  <div class="bg-slate-50 dark:bg-slate-950 font-sans text-slate-900 dark:text-slate-100 selection:bg-indigo-200 selection:text-indigo-900 antialiased overflow-x-hidden transition-colors duration-500">
    
    <nav 
      :class="[
        'fixed top-0 w-full z-[100] backdrop-blur-xl border-b transition-all duration-500',
        showNavbar ? 'translate-y-0 bg-white/70 dark:bg-slate-950/70 border-slate-200/50 dark:border-slate-800/50' : '-translate-y-full opacity-0'
      ]"
    >
      <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gradient-to-br from-indigo-500 to-blue-600 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-500/20">
            <i class="fas fa-lungs text-white text-lg"></i>
          </div>
          <span class="text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">Pneumo<span class="text-indigo-600 dark:text-indigo-400">Assist</span></span>
        </div>
        
        <div class="hidden lg:flex items-center gap-8 text-sm font-semibold text-slate-600 dark:text-slate-300">
          <a href="#solucao" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">A Solução</a>
          <a href="#tecnologia" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Tecnologia</a>
          <a href="#metodo" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Metodologia</a>
          <a href="#publico" class="hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Para Quem</a>
        </div>

        <div class="flex items-center gap-4">
          <NuxtLink to="/sobre" class="hidden md:block text-sm font-bold text-slate-600 dark:text-slate-300 hover:text-indigo-600 transition-colors">
            Sobre Nós
          </NuxtLink>
          <NuxtLink to="/chatbot" class="bg-slate-900 dark:bg-white text-white dark:text-slate-900 px-6 py-2.5 rounded-full text-sm font-bold hover:scale-105 hover:shadow-xl hover:shadow-slate-900/20 dark:hover:shadow-white/20 transition-all duration-300">
            Aceder Plataforma
          </NuxtLink>
        </div>
      </div>
    </nav>

    <header class="relative pt-40 pb-32 px-6 overflow-hidden">
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-5xl h-[600px] bg-gradient-to-b from-indigo-500/10 to-transparent dark:from-indigo-500/20 blur-[120px] rounded-full pointer-events-none"></div>
      <div class="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.03] dark:opacity-[0.05] pointer-events-none mix-blend-overlay"></div>

      <div class="max-w-7xl mx-auto grid lg:grid-cols-2 gap-16 items-center relative z-10 fade-in-up">
        <div class="space-y-8">
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-indigo-50 dark:bg-indigo-500/10 border border-indigo-100 dark:border-indigo-500/20 backdrop-blur-md">
            <span class="flex h-2 w-2 relative">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-indigo-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-indigo-500"></span>
            </span>
            <span class="text-xs font-bold uppercase tracking-wide text-indigo-700 dark:text-indigo-300">Llama 3.2 Vision Integrado</span>
          </div>
          
          <h1 class="text-5xl lg:text-7xl font-black text-slate-900 dark:text-white leading-[1.05] tracking-tight">
            A Nova Era da <br/>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-cyan-500">Triagem Pulmonar.</span>
          </h1>
          
          <p class="text-lg md:text-xl text-slate-600 dark:text-slate-400 max-w-xl leading-relaxed font-light">
            O primeiro co-piloto clínico impulsionado por visão computacional ultrarrápida. Analise radiografias e faça a triagem de sintomas em <strong>menos de 1 segundo</strong>.
          </p>
          
          <div class="flex flex-col sm:flex-row gap-4 pt-4">
            <NuxtLink to="/chatbot" class="px-8 py-4 bg-indigo-600 text-white text-center rounded-2xl font-bold text-base shadow-lg shadow-indigo-600/30 hover:shadow-indigo-600/50 hover:-translate-y-1 transition-all duration-300 flex items-center justify-center gap-2">
              Iniciar Análise Imediata <i class="fas fa-arrow-right text-sm"></i>
            </NuxtLink>
            <a href="#solucao" class="px-8 py-4 bg-white/50 dark:bg-slate-900/50 backdrop-blur-md text-slate-800 dark:text-white text-center rounded-2xl font-bold text-base border border-slate-200/50 dark:border-slate-700/50 hover:bg-white dark:hover:bg-slate-800 transition-all duration-300">
              Descobrir Mais
            </a>
          </div>
          
          <div class="pt-8 flex items-center gap-4 text-sm text-slate-500 dark:text-slate-400 font-medium border-t border-slate-200 dark:border-slate-800/50 max-w-md">
            <div class="flex -space-x-3">
              <img src="https://i.pravatar.cc/100?img=1" class="w-10 h-10 rounded-full border-2 border-slate-50 dark:border-slate-950" alt="Médico 1">
              <img src="https://i.pravatar.cc/100?img=2" class="w-10 h-10 rounded-full border-2 border-slate-50 dark:border-slate-950" alt="Médico 2">
              <img src="https://i.pravatar.cc/100?img=3" class="w-10 h-10 rounded-full border-2 border-slate-50 dark:border-slate-950" alt="Médico 3">
            </div>
            <span>Usado por +2.000 profissionais de saúde e centros clínicos ibéricos.</span>
          </div>
        </div>
        
        <div class="relative flex justify-center lg:justify-end">
          <div class="w-full max-w-lg bg-white/60 dark:bg-slate-900/60 backdrop-blur-2xl rounded-[2.5rem] border border-slate-200/50 dark:border-slate-800/50 p-6 shadow-2xl shadow-slate-300/50 dark:shadow-indigo-900/20 relative group">
            
            <div class="absolute -top-6 -left-8 bg-white dark:bg-slate-800 p-4 rounded-2xl shadow-xl border border-slate-100 dark:border-slate-700 animate-float z-20">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-emerald-100 dark:bg-emerald-900/30 flex items-center justify-center">
                  <i class="fas fa-check text-emerald-600 dark:text-emerald-400"></i>
                </div>
                <div>
                  <p class="text-sm font-bold text-slate-900 dark:text-white">Análise Concluída</p>
                  <p class="text-xs text-slate-500">Groq LPU: 0.8s</p>
                </div>
              </div>
            </div>

            <div class="bg-slate-50 dark:bg-slate-950 rounded-[1.5rem] overflow-hidden border border-slate-200 dark:border-slate-800 relative">
              <div class="h-12 bg-slate-100 dark:bg-slate-900 flex items-center px-4 gap-2">
                <div class="w-3 h-3 rounded-full bg-rose-400"></div>
                <div class="w-3 h-3 rounded-full bg-amber-400"></div>
                <div class="w-3 h-3 rounded-full bg-emerald-400"></div>
              </div>
              <div class="p-4 relative">
                <img src="https://images.unsplash.com/photo-1576086213369-97a306d36557?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" class="w-full h-auto aspect-[4/3] object-cover rounded-xl shadow-inner mix-blend-multiply dark:mix-blend-normal" alt="Raio-x interface" />
                <div class="absolute inset-x-4 top-4 h-full pointer-events-none overflow-hidden rounded-xl">
                  <div class="w-full h-1 bg-indigo-500 shadow-[0_0_15px_rgba(99,102,241,1)] animate-scan"></div>
                </div>
              </div>
              <div class="p-5 border-t border-slate-100 dark:border-slate-800">
                <div class="flex justify-between items-center mb-3">
                  <span class="text-xs font-bold text-slate-500 uppercase">Detecção Principal</span>
                  <span class="text-xs font-bold text-indigo-600 bg-indigo-50 dark:bg-indigo-900/30 px-2 py-1 rounded">Opacidade LLL</span>
                </div>
                <div class="h-2 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                  <div class="h-full bg-gradient-to-r from-indigo-500 to-cyan-400 w-[85%]"></div>
                </div>
                <p class="text-[10px] text-right mt-1 text-slate-400">Confiança da IA: 85%</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="py-10 border-y border-slate-200/50 dark:border-slate-800/50 bg-white/50 dark:bg-slate-900/20 backdrop-blur-sm">
      <div class="max-w-7xl mx-auto px-6">
        <p class="text-center text-xs font-bold text-slate-400 uppercase tracking-widest mb-6">Processamento de Alta Performance Construído Com</p>
        <div class="flex flex-wrap justify-center items-center gap-10 md:gap-16 opacity-50 hover:opacity-100 transition-opacity duration-500 grayscale hover:grayscale-0">
          <span class="font-black text-xl md:text-2xl tracking-tighter hover:text-blue-600 transition-colors cursor-default">META <span class="font-light">LLAMA 3.2</span></span>
          <span class="font-black text-xl md:text-2xl tracking-tighter hover:text-orange-500 transition-colors cursor-default">GROQ <span class="text-orange-500 text-sm align-top">LPU</span></span>
          <span class="font-black text-xl md:text-2xl tracking-tighter hover:text-green-500 transition-colors cursor-default">NUXT<span class="text-green-500 font-light">3</span></span>
          <span class="font-black text-xl md:text-2xl tracking-tighter hover:text-cyan-500 transition-colors cursor-default">TAILWIND<span class="font-light">CSS</span></span>
        </div>
      </div>
    </div>

    <section id="solucao" class="py-32 px-6 bg-white dark:bg-slate-950">
      <div class="max-w-7xl mx-auto">
        <div class="text-center max-w-3xl mx-auto mb-20 fade-in-up">
          <h2 class="text-sm font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-widest mb-3">O Paradigma Atual</h2>
          <h3 class="text-3xl md:text-5xl font-black text-slate-900 dark:text-white mb-6">Porque desenvolvemos o PneumoAssist?</h3>
          <p class="text-lg text-slate-600 dark:text-slate-400">Hospitais e clínicas lidam com volumes massivos de imagens médicas diariamente, resultando em fadiga clínica e potenciais atrasos no diagnóstico.</p>
        </div>

        <div class="grid md:grid-cols-2 gap-12 items-stretch">
          <div class="p-10 rounded-[2rem] bg-rose-50 dark:bg-rose-950/10 border border-rose-100 dark:border-rose-900/30">
            <div class="w-14 h-14 bg-rose-100 dark:bg-rose-900/50 rounded-2xl flex items-center justify-center mb-8">
              <i class="fas fa-triangle-exclamation text-rose-600 dark:text-rose-400 text-2xl"></i>
            </div>
            <h4 class="text-2xl font-bold text-slate-900 dark:text-white mb-4">O Desafio Tradicional</h4>
            <ul class="space-y-4 text-slate-700 dark:text-slate-300">
              <li class="flex items-start gap-3">
                <i class="fas fa-times text-rose-500 mt-1"></i>
                <span>Sobrecarga de exames radiológicos acumulados gerando <strong>gargalos no atendimento</strong>.</span>
              </li>
              <li class="flex items-start gap-3">
                <i class="fas fa-times text-rose-500 mt-1"></i>
                <span>Cansaço visual dos radiologistas, aumentando o risco de <strong>falsos negativos</strong> sutis.</span>
              </li>
              <li class="flex items-start gap-3">
                <i class="fas fa-times text-rose-500 mt-1"></i>
                <span>Ferramentas de IA antigas lentas e que necessitam de infraestrutura de servidor complexa.</span>
              </li>
            </ul>
          </div>

          <div class="p-10 rounded-[2rem] bg-indigo-50 dark:bg-indigo-950/20 border border-indigo-100 dark:border-indigo-900/30 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-64 h-64 bg-indigo-500/10 rounded-full blur-3xl"></div>
            <div class="w-14 h-14 bg-indigo-100 dark:bg-indigo-900/50 rounded-2xl flex items-center justify-center mb-8 relative z-10">
              <i class="fas fa-check-double text-indigo-600 dark:text-indigo-400 text-2xl"></i>
            </div>
            <h4 class="text-2xl font-bold text-slate-900 dark:text-white mb-4 relative z-10">A Abordagem PneumoAssist</h4>
            <ul class="space-y-4 text-slate-700 dark:text-slate-300 relative z-10">
              <li class="flex items-start gap-3">
                <i class="fas fa-check text-indigo-600 mt-1"></i>
                <span>Triagem prévia que <strong>sinaliza anomalias imediatamente</strong>, priorizando casos críticos na fila.</span>
              </li>
              <li class="flex items-start gap-3">
                <i class="fas fa-check text-indigo-600 mt-1"></i>
                <span>Rede neural validada para detecção de micro-opacidades atuando como <strong>segunda opinião (co-piloto)</strong>.</span>
              </li>
              <li class="flex items-start gap-3">
                <i class="fas fa-check text-indigo-600 mt-1"></i>
                <span>Inferência via Groq LPU que processa a imagem via nuvem em <strong>fração de segundos</strong>.</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section id="tecnologia" class="py-32 px-6 bg-slate-50 dark:bg-slate-900/30">
      <div class="max-w-7xl mx-auto">
        <div class="text-center max-w-3xl mx-auto mb-20 fade-in-up">
          <h2 class="text-sm font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-widest mb-3">Arsenal Tecnológico</h2>
          <h3 class="text-3xl md:text-5xl font-black text-slate-900 dark:text-white mb-6">Ferramentas de Precisão Clínica</h3>
          <p class="text-lg text-slate-600 dark:text-slate-400">Um ecossistema desenhado para a fiabilidade médica, embrulhado numa interface de utilizador imaculada.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6 auto-rows-[250px]">
          
          <div class="md:col-span-2 lg:col-span-2 row-span-2 p-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-[2rem] hover:shadow-2xl hover:shadow-indigo-500/10 transition-all duration-300 group overflow-hidden relative flex flex-col justify-end">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900/80 via-transparent to-transparent z-10"></div>
            <img src="https://images.unsplash.com/photo-1616012480717-fd9867059ca0?q=80&w=1025&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Médico a analisar tablet" class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
            <div class="relative z-20 text-white">
              <div class="w-12 h-12 bg-indigo-600 rounded-xl flex items-center justify-center mb-4">
                <i class="fas fa-x-ray text-xl"></i>
              </div>
              <h4 class="font-bold text-2xl mb-2">Análise de Imagem em Alta Resolução</h4>
              <p class="text-sm text-slate-200 leading-relaxed max-w-md">Processamento detalhado de Raio-X com suporte DICOM/JPEG para detecção de opacidades, derrames pleurais e anomalias estruturais com demarcação visual (heatmaps).</p>
            </div>
          </div>

          <div class="p-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-[2rem] hover:-translate-y-1 transition-all duration-300 flex flex-col">
            <div class="w-12 h-12 bg-emerald-50 dark:bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 rounded-xl flex items-center justify-center mb-auto">
              <i class="fas fa-bolt text-xl"></i>
            </div>
            <h4 class="font-bold text-lg text-slate-900 dark:text-white mt-4 mb-2">Velocidade Groq</h4>
            <p class="text-sm text-slate-600 dark:text-slate-400">Inferência LPU que entrega laudos preliminares de modelos massivos em tempo real.</p>
          </div>

          <div class="p-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-[2rem] hover:-translate-y-1 transition-all duration-300 flex flex-col">
            <div class="w-12 h-12 bg-amber-50 dark:bg-amber-500/10 text-amber-600 dark:text-amber-400 rounded-xl flex items-center justify-center mb-auto">
              <i class="fas fa-lock text-xl"></i>
            </div>
            <h4 class="font-bold text-lg text-slate-900 dark:text-white mt-4 mb-2">Privacidade LGPD</h4>
            <p class="text-sm text-slate-600 dark:text-slate-400">Anonimização de metadados na borda. Nenhum dado de paciente é retido na cloud.</p>
          </div>

          <div class="md:col-span-2 lg:col-span-2 p-8 bg-indigo-600 rounded-[2rem] hover:shadow-lg transition-all duration-300 relative overflow-hidden flex flex-col justify-center">
            <div class="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full blur-3xl pointer-events-none"></div>
            <div class="w-12 h-12 bg-white/20 text-white rounded-xl flex items-center justify-center mb-4">
              <i class="fas fa-file-medical text-xl"></i>
            </div>
            <h4 class="font-bold text-2xl text-white mb-2">Relatórios Estruturados Automáticos</h4>
            <p class="text-sm text-indigo-100 max-w-sm">Geração de sumários pré-formatados nos padrões clínicos internacionais prontos para revisão médica e anotação ao Prontuário Eletrônico do Paciente (PEP).</p>
          </div>

        </div>
      </div>
    </section>

    <section id="metodo" class="py-32 px-6 bg-slate-900 dark:bg-slate-950 text-white relative overflow-hidden border-y border-slate-800">
      <div class="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-[0.05] pointer-events-none mix-blend-overlay"></div>
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-indigo-600/10 rounded-full blur-[120px] pointer-events-none"></div>

      <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center mb-24 fade-in-up">
          <h2 class="text-sm font-bold text-indigo-400 uppercase tracking-widest mb-3">Workflow Sem Atrito</h2>
          <h3 class="text-3xl md:text-5xl font-black mb-6">Como o PneumoAssist Atua</h3>
          <p class="text-slate-400 text-lg max-w-2xl mx-auto">Integrando-se naturalmente na rotina. Sem instalações complexas. Aceda via browser e obtenha resultados.</p>
        </div>

        <div class="flex flex-col md:flex-row justify-between relative">
          <div class="hidden md:block absolute top-12 left-0 w-full h-0.5 bg-slate-800 z-0"></div>

          <div v-for="(step, i) in [
            { icon: 'fa-cloud-arrow-up', t: '1. Upload Seguro', d: 'Faça upload do exame ou introduza os sintomas no chat.' },
            { icon: 'fa-microchip', t: '2. Processamento IA', d: 'Llama 3.2 Vision analisa os píxeis e correlações clínicas.' },
            { icon: 'fa-eye', t: '3. Visão Didática', d: 'Visualização de heatmaps indicando as áreas suspeitas.' },
            { icon: 'fa-file-signature', t: '4. Apoio à Decisão', d: 'Receba o sumário formatado para agilizar o laudo final.' }
          ]" :key="i" class="relative z-10 flex-1 text-center group mb-12 md:mb-0 px-4">
            
            <div class="w-24 h-24 mx-auto bg-slate-900 border border-slate-700 rounded-full flex items-center justify-center mb-8 relative group-hover:border-indigo-500 transition-colors duration-500 shadow-xl shadow-black/50">
              <i :class="['fas text-2xl text-slate-400 group-hover:text-indigo-400 transition-colors duration-500', step.icon]"></i>
              <div class="absolute -right-2 -bottom-2 w-8 h-8 bg-indigo-600 text-white rounded-full flex items-center justify-center font-bold text-sm">
                {{ i + 1 }}
              </div>
            </div>
            
            <h4 class="font-bold text-xl mb-3">{{ step.t.split('. ')[1] }}</h4>
            <p class="text-slate-400 text-sm leading-relaxed max-w-[200px] mx-auto">{{ step.d }}</p>
          </div>
        </div>
      </div>
    </section>

    <section id="publico" class="py-24 px-6 bg-white dark:bg-slate-950">
      <div class="max-w-7xl mx-auto">
        <div class="grid lg:grid-cols-2 gap-16 items-center">
          <div>
            <h2 class="text-sm font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-widest mb-3">Versatilidade</h2>
            <h3 class="text-3xl md:text-4xl font-black text-slate-900 dark:text-white mb-8">Desenhado para todo o Ecossistema de Saúde</h3>
            
            <div class="space-y-6">
              <div class="flex gap-4 p-6 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-800 hover:border-indigo-500/30 transition-colors">
                <div class="w-12 h-12 shrink-0 bg-white dark:bg-slate-800 rounded-xl shadow-sm flex items-center justify-center">
                  <i class="fas fa-stethoscope text-indigo-600 dark:text-indigo-400 text-xl"></i>
                </div>
                <div>
                  <h4 class="font-bold text-lg text-slate-900 dark:text-white mb-2">Clínicos e Pneumologistas</h4>
                  <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">Confirmação de suspeitas e agilidade na redação de laudos durante as rondas ou em consultório privado.</p>
                </div>
              </div>

              <div class="flex gap-4 p-6 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-800 hover:border-indigo-500/30 transition-colors">
                <div class="w-12 h-12 shrink-0 bg-white dark:bg-slate-800 rounded-xl shadow-sm flex items-center justify-center">
                  <i class="fas fa-hospital text-indigo-600 dark:text-indigo-400 text-xl"></i>
                </div>
                <div>
                  <h4 class="font-bold text-lg text-slate-900 dark:text-white mb-2">Redes Hospitalares</h4>
                  <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">Integração via API para triagem automática no setor de urgências (PACS), definindo prioridades de atendimento.</p>
                </div>
              </div>

              <div class="flex gap-4 p-6 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-800 hover:border-indigo-500/30 transition-colors">
                <div class="w-12 h-12 shrink-0 bg-white dark:bg-slate-800 rounded-xl shadow-sm flex items-center justify-center">
                  <i class="fas fa-user-graduate text-indigo-600 dark:text-indigo-400 text-xl"></i>
                </div>
                <div>
                  <h4 class="font-bold text-lg text-slate-900 dark:text-white mb-2">Estudantes de Medicina</h4>
                  <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">Ferramenta educacional para treinar a visão radiológica. O chatbot explica o porquê de cada demarcação.</p>
                </div>
              </div>
            </div>
          </div>
          
          <div class="relative">
             <div class="absolute inset-0 bg-indigo-500/5 rounded-[3rem] transform rotate-3 scale-105"></div>
             <img src="https://images.unsplash.com/photo-1619691249147-c5689d88016b?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Médicos a discutir diagnóstico" class="relative rounded-[3rem] object-cover aspect-square md:aspect-[4/5] shadow-2xl z-10 border border-slate-200 dark:border-slate-800">
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 bg-gradient-to-br from-indigo-50 to-blue-50 dark:from-slate-900 dark:to-slate-900 border-y border-indigo-100/50 dark:border-slate-800 overflow-hidden relative">
      <div class="absolute top-0 right-0 w-[600px] h-[600px] bg-indigo-400/10 rounded-full blur-[100px] pointer-events-none"></div>
      
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center gap-16 relative z-10">
        <div class="flex-1 relative flex justify-center order-2 md:order-1">
          <div class="w-64 h-64 md:w-96 md:h-96 bg-white dark:bg-slate-800 rounded-[3rem] border-8 border-white/50 dark:border-slate-700/50 shadow-2xl shadow-indigo-500/20 flex items-center justify-center overflow-hidden animate-float">
            <img src="../public/mascoteimg/mascote.svg" alt="Dr. Brisa Mascote" class="w-full h-full object-cover" onerror="this.src='https://api.dicebear.com/7.x/bottts/svg?seed=Brisa&backgroundColor=e0e7ff'" />
          </div>
        </div>

        <div class="flex-1 text-center md:text-left space-y-6 order-1 md:order-2">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white dark:bg-slate-800 text-indigo-700 dark:text-indigo-300 text-xs font-bold uppercase tracking-widest shadow-sm">
            <i class="fas fa-robot text-indigo-500"></i> Interface Amigável
          </div>
          <h2 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-tight">
            Conheça o <span class="text-indigo-600 dark:text-indigo-400">Dr. Brisa</span>
          </h2>
          <p class="text-lg text-slate-600 dark:text-slate-400 leading-relaxed">
            A tecnologia não precisa ser assustadora. O nosso assistente virtual representa a união perfeita entre o acolhimento humano e o rigor matemático das redes neurais.
          </p>
          <ul class="space-y-4 pt-4">
            <li class="flex items-center gap-4 text-slate-800 dark:text-slate-200 font-medium">
              <div class="w-8 h-8 rounded-full bg-emerald-100 dark:bg-emerald-900/30 flex items-center justify-center text-emerald-600 dark:text-emerald-400"><i class="fas fa-check"></i></div>
              Acalma pacientes durante a pré-triagem de sintomas.
            </li>
            <li class="flex items-center gap-4 text-slate-800 dark:text-slate-200 font-medium">
              <div class="w-8 h-8 rounded-full bg-emerald-100 dark:bg-emerald-900/30 flex items-center justify-center text-emerald-600 dark:text-emerald-400"><i class="fas fa-check"></i></div>
              Linguagem adaptável: Técnica para médicos, simples para pacientes.
            </li>
          </ul>
        </div>
      </div>
    </section>

    <section class="py-32 px-6 bg-slate-50 dark:bg-slate-950">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-20 fade-in-up">
          <h2 class="text-sm font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-widest mb-3">Casos de Sucesso</h2>
          <h3 class="text-3xl md:text-5xl font-black text-slate-900 dark:text-white">Confiança Clínica Comprovada.</h3>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
          <div class="bg-white dark:bg-slate-900 p-8 rounded-[2rem] border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300">
            <div class="flex text-amber-400 text-sm mb-6 gap-1">
              <i class="fas fa-star" v-for="s in 5" :key="s"></i>
            </div>
            <p class="text-slate-700 dark:text-slate-300 mb-8 italic text-lg leading-relaxed">"A integração do PneumoAssist no plantão noturno reduziu nosso tempo de triagem radiológica em 40%. A assertividade das demarcações é notável, servindo como uma excelente rede de segurança."</p>
            <div class="flex items-center gap-4 border-t border-slate-100 dark:border-slate-800 pt-6">
              <img src="https://i.pravatar.cc/100?img=32" class="w-12 h-12 rounded-full object-cover" alt="Avatar">
              <div>
                <h4 class="font-bold text-slate-900 dark:text-white">Dr. Carlos Silva</h4>
                <p class="text-xs text-slate-500">Diretor Clínico, Hosp. São Paulo</p>
              </div>
            </div>
          </div>

          <div class="bg-white dark:bg-slate-900 p-8 rounded-[2rem] border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300 transform md:-translate-y-6">
            <div class="flex text-amber-400 text-sm mb-6 gap-1">
              <i class="fas fa-star" v-for="s in 5" :key="s"></i>
            </div>
            <p class="text-slate-700 dark:text-slate-300 mb-8 italic text-lg leading-relaxed">"Uso a plataforma diariamente no consultório. Os relatórios estruturados gerados pela IA poupam-me pelo menos 2 horas de documentação por semana. A interface é incrivelmente rápida."</p>
            <div class="flex items-center gap-4 border-t border-slate-100 dark:border-slate-800 pt-6">
              <img src="https://i.pravatar.cc/100?img=44" class="w-12 h-12 rounded-full object-cover" alt="Avatar">
              <div>
                <h4 class="font-bold text-slate-900 dark:text-white">Dra. Sofia Mendonça</h4>
                <p class="text-xs text-slate-500">Pneumologista Especialista</p>
              </div>
            </div>
          </div>

          <div class="bg-white dark:bg-slate-900 p-8 rounded-[2rem] border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-xl hover:-translate-y-2 transition-all duration-300">
            <div class="flex text-amber-400 text-sm mb-6 gap-1">
              <i class="fas fa-star" v-for="s in 5" :key="s"></i>
            </div>
            <p class="text-slate-700 dark:text-slate-300 mb-8 italic text-lg leading-relaxed">"Como estudante do 5º ano, o chatbot educativo do Dr. Brisa tem sido fundamental para treinar meu olho clínico. Ele não apenas aponta o erro, ele explica a fisiopatologia."</p>
            <div class="flex items-center gap-4 border-t border-slate-100 dark:border-slate-800 pt-6">
              <img src="https://i.pravatar.cc/100?img=12" class="w-12 h-12 rounded-full object-cover" alt="Avatar">
              <div>
                <h4 class="font-bold text-slate-900 dark:text-white">João Pedro Costa</h4>
                <p class="text-xs text-slate-500">Estudante de Medicina (FMUP)</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 bg-slate-50 dark:bg-slate-900/30 border-y border-slate-200 dark:border-slate-800">
      <div class="max-w-3xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-black text-slate-900 dark:text-white">Perguntas Frequentes</h2>
        </div>
        <div class="space-y-4">
          <details class="group bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-sm [&_summary::-webkit-details-marker]:hidden open:shadow-md transition-shadow">
            <summary class="flex items-center justify-between p-6 cursor-pointer font-bold text-lg text-slate-900 dark:text-white">
              A IA substitui o diagnóstico do médico?
              <span class="transition-transform duration-300 group-open:-rotate-180 bg-slate-100 dark:bg-slate-800 w-8 h-8 rounded-full flex items-center justify-center"><i class="fas fa-chevron-down text-indigo-500 text-sm"></i></span>
            </summary>
            <div class="px-6 pb-6 text-slate-600 dark:text-slate-400 leading-relaxed border-t border-slate-100 dark:border-slate-800 pt-4 mt-2">
              Absolutamente não. O PneumoAssist é legalmente classificado como um Sistema de Apoio à Decisão Clínica (CDSS). Atuamos como uma "segunda opinião instantânea" para sinalizar anomalias e agilizar o processo, mas o diagnóstico definitivo e a conduta terapêutica são de inteira responsabilidade do profissional de saúde.
            </div>
          </details>
          
          <details class="group bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-sm [&_summary::-webkit-details-marker]:hidden open:shadow-md transition-shadow">
            <summary class="flex items-center justify-between p-6 cursor-pointer font-bold text-lg text-slate-900 dark:text-white">
              Os dados dos meus pacientes estão seguros?
              <span class="transition-transform duration-300 group-open:-rotate-180 bg-slate-100 dark:bg-slate-800 w-8 h-8 rounded-full flex items-center justify-center"><i class="fas fa-chevron-down text-indigo-500 text-sm"></i></span>
            </summary>
            <div class="px-6 pb-6 text-slate-600 dark:text-slate-400 leading-relaxed border-t border-slate-100 dark:border-slate-800 pt-4 mt-2">
              Sim. Cumprimos rigorosamente a LGPD e a HIPAA. A nossa tecnologia limpa automaticamente os metadados (DICOM tags) que identificam o paciente no seu browser, <strong>antes</strong> de enviar a imagem para o servidor de inferência. Nenhuma imagem é guardada para treino de IA sem o expresso consentimento institucional.
            </div>
          </details>

          <details class="group bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-sm [&_summary::-webkit-details-marker]:hidden open:shadow-md transition-shadow">
            <summary class="flex items-center justify-between p-6 cursor-pointer font-bold text-lg text-slate-900 dark:text-white">
              Preciso de instalar algum software no hospital?
              <span class="transition-transform duration-300 group-open:-rotate-180 bg-slate-100 dark:bg-slate-800 w-8 h-8 rounded-full flex items-center justify-center"><i class="fas fa-chevron-down text-indigo-500 text-sm"></i></span>
            </summary>
            <div class="px-6 pb-6 text-slate-600 dark:text-slate-400 leading-relaxed border-t border-slate-100 dark:border-slate-800 pt-4 mt-2">
              Para o uso do plano "Clínico Pro" ou "Básico", basta um navegador web moderno (Chrome, Safari, Edge). Para o plano "Hospitalar", oferecemos APIs REST seguras e conectores HL7/DICOM para integração direta no sistema PACS do hospital, permitindo um fluxo totalmente automatizado.
            </div>
          </details>
        </div>
      </div>
    </section>

    <section class="py-32 px-6 bg-white dark:bg-slate-950">
      <div class="max-w-5xl mx-auto bg-[url('https://grainy-gradients.vercel.app/noise.svg')] bg-indigo-600 rounded-[3rem] p-12 md:p-20 text-center shadow-2xl shadow-indigo-600/30 relative overflow-hidden">
        <div class="absolute inset-0 mix-blend-overlay opacity-50 bg-gradient-to-br from-indigo-500 to-blue-800 pointer-events-none"></div>
        <div class="absolute -top-24 -right-24 w-96 h-96 bg-white/10 rounded-full blur-3xl pointer-events-none"></div>
        
        <h2 class="text-4xl md:text-5xl font-black text-white mb-6 relative z-10 tracking-tight">Pronto para transformar sua rotina clínica?</h2>
        <p class="text-xl text-indigo-100 mb-10 max-w-2xl mx-auto relative z-10 font-light">Crie a sua conta gratuitamente em menos de 1 minuto e faça o seu primeiro upload para ver o Llama 3.2 Vision em ação.</p>
        
        <NuxtLink to="/chatbot" class="relative z-10 inline-flex items-center gap-3 bg-white text-indigo-700 px-10 py-5 rounded-2xl font-black text-lg shadow-xl hover:shadow-2xl hover:bg-slate-50 hover:scale-105 transition-all duration-300">
          <i class="fas fa-rocket text-indigo-500"></i> Acessar Plataforma Agora
        </NuxtLink>
      </div>
    </section>

    <footer ref="footerElement" class="bg-slate-950 text-slate-300 py-24 px-6 border-t border-slate-800">
      <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-16">
        <div class="col-span-1 lg:col-span-2 space-y-8">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 bg-gradient-to-br from-indigo-500 to-blue-600 rounded-xl flex items-center justify-center">
              <i class="fas fa-lungs text-white text-xl"></i>
            </div>
            <span class="font-black text-3xl text-white">Pneumo<span class="text-indigo-400">Assist</span></span>
          </div>
          <p class="text-base text-slate-400 max-w-sm leading-relaxed">
            Ferramenta de apoio clínico baseada em Inteligência Artificial para análise avançada de imagem e triagem pulmonar. Desenvolvido para salvar tempo e vidas.
          </p>
          
          <div class="pt-2">
            <p class="text-xs font-bold uppercase tracking-widest text-slate-500 mb-4">Newsletter Científica</p>
            <div class="flex gap-2 max-w-sm">
              <input type="email" placeholder="seu@email.com" class="bg-slate-900 border border-slate-800 rounded-xl px-4 py-3 text-sm w-full focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all text-white placeholder-slate-600">
              <button class="bg-indigo-600 hover:bg-indigo-500 text-white px-6 py-3 rounded-xl text-sm font-bold transition-colors">Assinar</button>
            </div>
          </div>
        </div>
        
        <div>
          <h4 class="text-sm font-black text-white uppercase tracking-widest mb-6">Produto</h4>
          <ul class="space-y-4 text-sm text-slate-400 font-medium">
            <li><NuxtLink to="/chatbot" class="hover:text-indigo-400 transition-colors">Plataforma Vision</NuxtLink></li>
            <li><a href="#solucao" class="hover:text-indigo-400 transition-colors">O Desafio</a></li>
            <li><a href="#metodo" class="hover:text-indigo-400 transition-colors">Como Funciona</a></li>
            <li><a href="#precos" class="hover:text-indigo-400 transition-colors">Planos e Preços</a></li>
          </ul>
        </div>
        
        <div>
          <h4 class="text-sm font-black text-white uppercase tracking-widest mb-6">Empresa</h4>
          <ul class="space-y-4 text-sm text-slate-400 font-medium">
            <li><NuxtLink to="/sobre" class="hover:text-indigo-400 transition-colors">Sobre Nós (Equipe)</NuxtLink></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Carreiras</a></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Blog Médico</a></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Contato Comercial</a></li>
          </ul>
        </div>
        
        <div>
          <h4 class="text-sm font-black text-white uppercase tracking-widest mb-6">Legal & Social</h4>
          <ul class="space-y-4 text-sm text-slate-400 font-medium">
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Política de Privacidade</a></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Termos de Uso</a></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Compliance & LGPD</a></li>
          </ul>
          
          <div class="flex gap-4 mt-8">
            <a href="#" class="w-10 h-10 rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-400 hover:text-white hover:bg-indigo-600 hover:border-indigo-600 transition-all"><i class="fab fa-linkedin-in"></i></a>
            <a href="#" class="w-10 h-10 rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-400 hover:text-white hover:bg-indigo-600 hover:border-indigo-600 transition-all"><i class="fab fa-twitter"></i></a>
            <a href="#" class="w-10 h-10 rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-400 hover:text-white hover:bg-indigo-600 hover:border-indigo-600 transition-all"><i class="fab fa-instagram"></i></a>
          </div>
        </div>
      </div>
      
      <div class="max-w-7xl mx-auto mt-20 pt-8 border-t border-slate-800/50 flex flex-col md:flex-row items-center justify-between gap-4">
        <p class="text-sm text-slate-500 font-medium">&copy; {{ new Date().getFullYear() }} PneumoAssist Technologies. Todos os direitos reservados.</p>
        <div class="flex items-center gap-2 text-sm font-medium text-slate-500">
          Criado com rigor clínico e <i class="fas fa-heart text-rose-500"></i>
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

// Transição de página fluída estilo "Slide" nativa do Nuxt 3
definePageMeta({
  pageTransition: {
    name: 'slide',
    mode: 'out-in'
  }
})

// SEO e Meta Tags
useHead({
  title: 'PneumoAssist | A Nova Era da Triagem Pulmonar',
  meta: [
    { name: 'description', content: 'Assistente clínico avançado de visão computacional para triagem respiratória com Llama 3.2 Vision e Groq. Rápido, seguro e preciso.' }
  ],
  link: [
    { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' }
  ]
})

// Lógica para esconder Navbar no Footer (mantida)
const footerElement = ref(null)
const showNavbar = ref(true)
let observer: IntersectionObserver | null = null

onMounted(() => {
  observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      showNavbar.value = !entry.isIntersecting
    })
  }, { 
    threshold: 0.1 
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

/* Page Transitions do Nuxt 3 
  Isso cria o efeito de 'slide' sempre que mudar de rota
*/
.slide-enter-active,
.slide-leave-active {
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.slide-enter-from {
  opacity: 0;
  transform: translateX(30px);
}
.slide-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

/* Animações Nativas Avançadas */
.animate-float {
  animation: float 6s ease-in-out infinite;
}
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-15px); }
  100% { transform: translateY(0px); }
}

.animate-scan {
  animation: scan 3s linear infinite;
}
@keyframes scan {
  0% { transform: translateY(0); opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { transform: translateY(1000%); opacity: 0; }
}

.fade-in-up {
  animation: fadeInUp 1s ease-out forwards;
  opacity: 0;
}
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(30px); }
  100% { opacity: 1; transform: translateY(0); }
}

/* Custom Scrollbar para melhorar o feel profissional */
::-webkit-scrollbar {
  width: 10px;
}
::-webkit-scrollbar-track {
  @apply bg-slate-100 dark:bg-slate-900;
}
::-webkit-scrollbar-thumb {
  @apply bg-slate-300 dark:bg-slate-700 rounded-full;
}
::-webkit-scrollbar-thumb:hover {
  @apply bg-slate-400 dark:bg-slate-600;
}
</style>