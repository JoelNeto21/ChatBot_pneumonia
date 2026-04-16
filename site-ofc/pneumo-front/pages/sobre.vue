<template>
  <div class="bg-slate-50 dark:bg-slate-950 font-sans text-slate-900 dark:text-slate-100 antialiased selection:bg-indigo-500/30 selection:text-indigo-900 dark:selection:text-indigo-100 min-h-screen flex flex-col overflow-x-hidden transition-colors duration-500">
    
    <nav 
      :class="[
        'fixed top-0 w-full z-[100] transition-all duration-500 ease-in-out',
        showNavbar ? 'translate-y-0' : '-translate-y-full',
        isScrolled ? 'bg-white/80 dark:bg-slate-950/80 backdrop-blur-xl border-b border-slate-200/50 dark:border-slate-800/50 shadow-sm' : 'bg-transparent border-transparent'
      ]"
    >
      <div class="max-w-7xl mx-auto px-6 flex items-center justify-between transition-all duration-500" :class="isScrolled ? 'h-20' : 'h-24'">
        <NuxtLink to="/" class="flex items-center gap-3 group">
          <div class="w-10 h-10 bg-gradient-to-br from-indigo-500 to-blue-600 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-500/20 group-hover:scale-110 group-hover:rotate-3 transition-all duration-300">
            <i class="fas fa-lungs text-white text-lg"></i>
          </div>
          <span class="text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">
            Pneumo<span class="text-indigo-600 dark:text-indigo-500">Assist</span>
          </span>
        </NuxtLink>
        <div class="flex items-center gap-8">
          <NuxtLink to="/" class="hidden sm:block text-sm font-bold text-slate-500 dark:text-slate-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">
            Voltar ao Início
          </NuxtLink>
          <NuxtLink to="/chatbot" class="relative group overflow-hidden rounded-xl">
            <div class="absolute inset-0 bg-gradient-to-r from-indigo-600 to-blue-600 group-hover:opacity-90 transition-opacity duration-300"></div>
            <div class="relative bg-slate-900 dark:bg-white text-white dark:text-slate-900 px-6 py-2.5 rounded-xl text-sm font-bold group-hover:bg-transparent group-hover:text-white dark:group-hover:bg-transparent transition-all shadow-lg shadow-indigo-500/25">
              Aceder Plataforma
            </div>
          </NuxtLink>
        </div>
      </div>
    </nav>

    <header class="relative pt-40 pb-20 md:pt-48 md:pb-32 px-6 overflow-hidden flex items-center min-h-[85vh]">
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_-20%,_var(--tw-gradient-stops))] from-indigo-100/40 via-transparent to-transparent dark:from-indigo-900/20 -z-10"></div>
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full bg-grid opacity-50 dark:opacity-20 -z-10"></div>

      <div class="max-w-7xl mx-auto w-full grid lg:grid-cols-2 gap-12 lg:gap-8 items-center relative z-10">
        <div class="animate-reveal reveal-left">
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-indigo-50 dark:bg-indigo-500/10 border border-indigo-100 dark:border-indigo-500/20 text-indigo-600 dark:text-indigo-400 text-xs font-bold uppercase tracking-wider mb-8 shadow-sm">
            <span class="relative flex h-2 w-2 mr-1">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-indigo-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-indigo-500"></span>
            </span>
            Manifesto Institucional
          </div>
          
          <h1 class="text-5xl md:text-6xl lg:text-7xl font-extrabold text-slate-900 dark:text-white mb-6 tracking-tight leading-[1.1]">
            Onde a medicina <br class="hidden lg:block" />
            encontra o <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-blue-500 animate-gradient">futuro.</span>
          </h1>
          
          <p class="text-lg md:text-xl text-slate-600 dark:text-slate-400 leading-relaxed mb-8 max-w-lg font-medium">
            O PneumoAssist não é apenas um software. É um ecossistema de inteligência artificial de baixa latência desenhado para revolucionar a forma como os profissionais de saúde interpretam exames radiológicos.
          </p>

          <div class="flex flex-wrap items-center gap-4">
            <div class="flex -space-x-4">
              <img src="https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&q=80&w=100&h=100" class="w-12 h-12 rounded-full border-2 border-white dark:border-slate-900 object-cover" />
              <img src="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&q=80&w=100&h=100" class="w-12 h-12 rounded-full border-2 border-white dark:border-slate-900 object-cover" />
              <img src="https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&q=80&w=100&h=100" class="w-12 h-12 rounded-full border-2 border-white dark:border-slate-900 object-cover" />
            </div>
            <div class="text-sm font-medium text-slate-600 dark:text-slate-400">
              Junte-se a dezenas de especialistas.
            </div>
          </div>
        </div>

        <div class="relative animate-reveal reveal-right hidden md:block">
          <div class="relative aspect-[4/3] rounded-[2rem] overflow-hidden shadow-2xl border border-slate-200/50 dark:border-slate-800 bg-slate-900">
            <img src="https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&q=80&w=1200" class="w-full h-full object-cover opacity-80 mix-blend-luminosity hover:mix-blend-normal transition-all duration-700" alt="Medicina Tecnológica" />
            <div class="absolute inset-0 bg-gradient-to-tr from-indigo-900/60 to-transparent"></div>
            
            <div class="absolute bottom-6 right-6 bg-white/10 backdrop-blur-md border border-white/20 p-4 rounded-xl">
              <i class="fas fa-microchip text-white text-2xl mb-2"></i>
              <p class="text-white text-sm font-bold">Processamento LPU</p>
            </div>
          </div>

          <div class="absolute -bottom-8 -left-8 bg-white dark:bg-slate-900 p-5 rounded-2xl shadow-xl border border-slate-100 dark:border-slate-800 animate-float">
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-indigo-50 dark:bg-indigo-500/10 rounded-xl flex items-center justify-center text-indigo-600 dark:text-indigo-400">
                <i class="fas fa-shield-alt text-xl"></i>
              </div>
              <div>
                <p class="text-sm font-bold text-slate-900 dark:text-white">Segurança de Dados</p>
                <p class="text-xs text-slate-500">Conformidade total</p>
              </div>
            </div>
          </div>

          <div class="absolute -top-6 -right-6 bg-white dark:bg-slate-900 p-4 rounded-xl shadow-lg border border-slate-100 dark:border-slate-800 animate-float" style="animation-delay: 1.5s;">
            <div class="flex items-center gap-3">
              <div class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
              <p class="text-xs font-bold text-slate-900 dark:text-white uppercase tracking-wider">Sistema Online</p>
            </div>
          </div>
        </div>
      </div>
    </header>

    <section class="py-24 px-6 relative z-20 border-t border-slate-200/50 dark:border-slate-800/50 bg-white dark:bg-slate-950/50">
      <div class="max-w-7xl mx-auto">
        <div class="grid lg:grid-cols-2 gap-16 items-center">
          <div class="animate-reveal reveal-left">
            <h2 class="text-sm font-black text-indigo-600 dark:text-indigo-500 uppercase tracking-widest mb-4 flex items-center gap-2">
              <i class="fas fa-bullseye"></i> Por que existimos?
            </h2>
            <h3 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white mb-6 tracking-tight leading-tight">
              O gargalo no diagnóstico <br>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-rose-500 to-orange-500">respiratório de urgência.</span>
            </h3>
            <p class="text-slate-600 dark:text-slate-400 leading-relaxed text-lg mb-8">
              Todos os anos, milhões de diagnósticos de pneumonia e patologias associadas sofrem atrasos devido à sobrecarga dos sistemas de saúde e à falta de radiologistas disponíveis 24/7. O tempo perdido na triagem é tempo perdido na terapêutica.
            </p>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 animate-reveal reveal-right">
            <div v-for="(stat, index) in stats" :key="index" class="p-8 bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800/80 rounded-[2rem] hover:-translate-y-2 hover:shadow-2xl hover:shadow-indigo-500/10 transition-all duration-300 relative overflow-hidden group">
              <div class="absolute inset-0 bg-gradient-to-br from-indigo-50 to-transparent dark:from-indigo-500/5 dark:to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
              <h4 class="text-4xl md:text-5xl font-black text-indigo-600 dark:text-indigo-400 mb-4 relative z-10">{{ stat.num }}</h4>
              <p class="text-sm text-slate-500 dark:text-slate-400 font-medium leading-relaxed relative z-10">{{ stat.text }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 bg-slate-50 dark:bg-[#0B0E14] border-y border-slate-200/50 dark:border-slate-800/50 overflow-hidden relative">
      <div class="max-w-7xl mx-auto grid lg:grid-cols-2 gap-20 items-center relative z-10">
        
        <div class="space-y-8 animate-reveal reveal-left">
          <div class="inline-flex items-center gap-3">
            <div class="h-[2px] w-12 bg-indigo-600"></div>
            <h2 class="text-sm font-black text-indigo-600 uppercase tracking-widest">A Arquitetura Tecnológica</h2>
          </div>
          <h3 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white leading-[1.1]">
            Poder de processamento no limite do hardware.
          </h3>
          <p class="text-slate-600 dark:text-slate-400 leading-relaxed text-lg">
            A latência é o maior inimigo na urgência médica. Por isso, a nossa infraestrutura corre em LPUs comunicando com um frontend Nuxt/Vue isomórfico extremamente leve, garantindo respostas sub-segundo.
          </p>
          
          <div class="pt-6">
            <p class="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-widest mb-4">Core Stack</p>
            <div class="flex flex-wrap gap-2.5">
              <span v-for="tech in techStack" :key="tech" class="px-4 py-2 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl text-sm font-semibold text-slate-700 dark:text-slate-300 hover:border-indigo-500 hover:text-indigo-600 dark:hover:text-indigo-400 transition-all cursor-default shadow-sm hover:shadow-md">
                {{ tech }}
              </span>
            </div>
          </div>
        </div>

        <div class="relative w-full aspect-square md:aspect-[4/3] rounded-[2.5rem] bg-slate-900 border border-slate-800 overflow-hidden animate-reveal reveal-right shadow-2xl group">
          <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1530497610245-94d3c16cda28?auto=format&fit=crop&q=80&w=1000')] bg-cover bg-center opacity-30 mix-blend-screen group-hover:scale-105 transition-transform duration-1000"></div>
          <div class="absolute inset-0 bg-indigo-900/40 mix-blend-multiply"></div>
          
          <div class="absolute inset-0 pointer-events-none z-20">
            <div class="w-full h-1 bg-indigo-400 shadow-[0_0_20px_5px_rgba(99,102,241,0.5)] animate-scan"></div>
          </div>
          
          <div class="absolute inset-0 flex flex-col items-center justify-center z-30 p-8">
            <div class="grid grid-cols-2 gap-4 w-full">
               <div v-for="(metrica, index) in metricas" :key="index" class="p-6 rounded-2xl bg-slate-950/80 backdrop-blur-md border border-slate-800/80 hover:border-indigo-500/50 transition-colors">
                <p class="text-xs font-bold text-slate-400 mb-1 uppercase tracking-wider">{{ metrica.label }}</p>
                <h4 class="text-2xl md:text-3xl font-black text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-blue-400">{{ metrica.valor }}</h4>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 relative bg-white dark:bg-slate-950/50">
      <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center max-w-3xl mx-auto mb-20 animate-reveal reveal-up">
          <h2 class="text-sm font-black text-indigo-600 uppercase tracking-widest mb-4">Pipeline de Inferência</h2>
          <h3 class="text-3xl md:text-4xl font-black text-slate-900 dark:text-white tracking-tight">Como a IA interpreta as imagens</h3>
        </div>

        <div class="grid md:grid-cols-3 gap-8 relative">
          <div class="hidden md:block absolute top-12 left-[15%] right-[15%] h-[2px] bg-slate-200 dark:bg-slate-800 z-0">
            <div class="h-full w-full bg-gradient-to-r from-transparent via-indigo-500 to-transparent opacity-50 animate-pulse"></div>
          </div>
          
          <div v-for="(passo, index) in processos" :key="index" class="relative group animate-reveal reveal-up" :style="{ transitionDelay: `${index * 150}ms` }">
            <div class="relative z-10 bg-white dark:bg-[#11151F] p-8 md:p-10 rounded-[2.5rem] border border-slate-100 dark:border-slate-800 shadow-xl shadow-slate-200/50 dark:shadow-none h-full transition-all duration-300 group-hover:border-indigo-500/50 group-hover:-translate-y-3">
              <div class="w-20 h-20 bg-slate-50 dark:bg-slate-900 rounded-2xl flex items-center justify-center text-4xl font-black text-slate-300 dark:text-slate-700 mb-8 group-hover:bg-gradient-to-br group-hover:from-indigo-500 group-hover:to-blue-600 group-hover:text-white transition-all duration-300 shadow-inner">
                {{ passo.step }}
              </div>
              <h4 class="text-xl font-bold text-slate-900 dark:text-white mb-4">{{ passo.titulo }}</h4>
              <p class="text-slate-600 dark:text-slate-400 leading-relaxed text-sm">{{ passo.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 relative bg-slate-50 dark:bg-slate-950 border-t border-slate-200/50 dark:border-slate-800/50">
      <div class="max-w-4xl mx-auto">
        <div class="text-center mb-20 animate-reveal reveal-up">
          <h2 class="text-sm font-black text-indigo-600 uppercase tracking-widest mb-4 flex items-center justify-center gap-2">
            <i class="fas fa-clock"></i> A Evolução do Projeto
          </h2>
          <h3 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white tracking-tight">Da Ideia à Realidade Clínica</h3>
        </div>

        <div class="relative border-l-4 border-indigo-200 dark:border-slate-800 ml-6 md:ml-12 space-y-16">
          <div v-for="(item, index) in timeline" :key="index" class="relative pl-10 md:pl-16 animate-reveal reveal-up" :style="{ transitionDelay: `${index * 150}ms` }">
            <div class="absolute -left-[14px] top-1 w-6 h-6 rounded-full bg-indigo-500 border-4 border-slate-50 dark:border-slate-950 shadow-[0_0_15px_rgba(99,102,241,0.5)]"></div>
            <span class="text-sm font-black text-indigo-600 dark:text-indigo-400 tracking-widest uppercase bg-indigo-100 dark:bg-indigo-900/30 px-3 py-1 rounded-full">{{ item.ano }}</span>
            <h4 class="text-2xl font-bold text-slate-900 dark:text-white mt-4 mb-3">{{ item.titulo }}</h4>
            <p class="text-slate-600 dark:text-slate-400 text-lg leading-relaxed">{{ item.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="py-32 px-6 bg-white dark:bg-[#080A0F] border-t border-slate-200/50 dark:border-slate-800/50 relative overflow-hidden">
      <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center max-w-2xl mx-auto mb-20 animate-reveal reveal-up">
          <h2 class="text-sm font-black text-indigo-600 uppercase tracking-widest mb-4">Board de Engenharia & Medicina</h2>
          <h3 class="text-4xl md:text-5xl font-black text-slate-900 dark:text-white mb-6 tracking-tight">Mentes por Trás do Código</h3>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div v-for="(membro, index) in equipa" :key="index" class="relative p-[2px] rounded-[2.5rem] bg-gradient-to-b from-slate-200 to-white dark:from-slate-800 dark:to-[#11151F] hover:from-indigo-500 hover:to-blue-600 transition-all duration-500 group animate-reveal reveal-up" :style="{ transitionDelay: `${index * 100}ms` }">
            <div class="bg-slate-50 dark:bg-[#11151F] rounded-[2.4rem] p-8 h-full relative overflow-hidden text-center flex flex-col">
              
              <div class="absolute top-0 left-1/2 -translate-x-1/2 w-32 h-32 bg-indigo-500/20 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>

              <div class="relative z-10 flex-grow">
                <div class="w-32 h-32 mx-auto rounded-full p-2 border-2 border-slate-200 dark:border-slate-700 group-hover:border-transparent transition-colors duration-500 mb-6 relative">
                  <div class="w-full h-full rounded-full overflow-hidden bg-slate-100 dark:bg-slate-800 flex items-center justify-center">
                    <img :src="membro.foto" :alt="membro.nome" class="w-24 h-24 object-contain group-hover:scale-110 transition-transform duration-500 filter drop-shadow-md" />
                  </div>
                  <div :class="`absolute bottom-0 right-0 w-10 h-10 ${membro.corCorpo} text-white rounded-full flex items-center justify-center border-4 border-slate-50 dark:border-[#11151F] shadow-lg`">
                    <i :class="membro.icone + ' text-sm'"></i>
                  </div>
                </div>
                
                <h4 class="text-xl font-bold text-slate-900 dark:text-white">{{ membro.nome }}</h4>
                <p class="text-xs font-black text-indigo-600 dark:text-indigo-400 uppercase tracking-widest mt-2 mb-5">{{ membro.cargo }}</p>
                <p class="text-sm text-slate-500 dark:text-slate-400 mb-8 line-clamp-3 leading-relaxed">
                  {{ membro.bio }}
                </p>
              </div>

              <div class="flex justify-center gap-3 mt-auto relative z-10">
                <a :href="membro.github" target="_blank" class="w-10 h-10 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 flex items-center justify-center text-slate-400 hover:text-white hover:bg-slate-900 dark:hover:bg-white dark:hover:text-slate-900 transition-all duration-300"><i class="fab fa-github"></i></a>
                <a :href="membro.linkedin" target="_blank" class="w-10 h-10 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 flex items-center justify-center text-slate-400 hover:text-white hover:bg-[#0a66c2] dark:hover:bg-[#0a66c2] transition-all duration-300"><i class="fab fa-linkedin-in"></i></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="py-24 px-6 relative overflow-hidden bg-slate-50 dark:bg-[#0B0E14]">
      <div class="max-w-5xl mx-auto bg-slate-900 dark:bg-[#11151F] border border-slate-800 rounded-[3rem] p-12 md:p-24 text-center relative overflow-hidden shadow-2xl animate-reveal reveal-zoom">
        <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/20 to-blue-600/10 mix-blend-overlay"></div>
        <div class="absolute -top-32 -right-32 w-96 h-96 bg-indigo-500/30 rounded-full blur-[100px] animate-float"></div>
        <div class="absolute -bottom-32 -left-32 w-96 h-96 bg-blue-500/20 rounded-full blur-[100px] animate-float" style="animation-delay: -3s;"></div>
        
        <h2 class="text-4xl md:text-6xl font-black text-white mb-6 relative z-10 leading-tight tracking-tight">
          Experimente a triagem do <br class="hidden md:block"/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-blue-400">futuro, hoje.</span>
        </h2>
        <p class="text-slate-400 mb-12 text-lg md:text-xl max-w-2xl mx-auto relative z-10 font-medium">
          Acesse ao ambiente restrito e valide as respostas da IA com os seus próprios exames radiológicos e casos clínicos.
        </p>
        <div class="flex flex-col sm:flex-row justify-center gap-4 relative z-10">
          <NuxtLink to="/chatbot" class="bg-indigo-600 hover:bg-indigo-500 text-white px-10 py-5 rounded-2xl font-bold text-lg transition-all duration-300 shadow-[0_0_40px_-10px_rgba(79,70,229,0.5)] hover:shadow-[0_0_60px_-15px_rgba(79,70,229,0.7)] hover:-translate-y-1">
            Acessar Laboratório IA
          </NuxtLink>
        </div>
      </div>
    </section>

    <footer class="bg-slate-950 text-slate-300 py-24 px-6 border-t border-slate-800 relative z-20">
      <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-16">
        <div class="col-span-1 lg:col-span-2 space-y-8">
          <div class="flex items-center gap-3 group cursor-pointer">
            <div class="w-12 h-12 bg-gradient-to-br from-indigo-500 to-blue-600 rounded-xl flex items-center justify-center group-hover:scale-105 transition-transform">
              <i class="fas fa-lungs text-white text-xl"></i>
            </div>
            <span class="font-black text-3xl text-white tracking-tight">Pneumo<span class="text-indigo-400">Assist</span></span>
          </div>
          <p class="text-base text-slate-400 max-w-sm leading-relaxed">
            Ferramenta de apoio clínico baseada em Inteligência Artificial para análise avançada de imagem e triagem pulmonar. Desenvolvido para salvar tempo e vidas.
          </p>
          <div class="pt-2">
            <p class="text-xs font-bold uppercase tracking-widest text-slate-500 mb-4">Newsletter Científica</p>
            <div class="flex gap-2 max-w-sm">
              <input type="email" placeholder="seu@email.com" class="bg-slate-900 border border-slate-800 rounded-xl px-4 py-3.5 text-sm w-full focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all text-white placeholder-slate-600">
              <button class="bg-indigo-600 hover:bg-indigo-500 text-white px-6 py-3.5 rounded-xl text-sm font-bold transition-colors">Assinar</button>
            </div>
          </div>
        </div>
        
        <div>
          <h4 class="text-sm font-black text-white uppercase tracking-widest mb-6">Produto</h4>
          <ul class="space-y-4 text-sm text-slate-400 font-medium">
            <li><NuxtLink to="/chatbot" class="hover:text-indigo-400 transition-colors">Plataforma Vision</NuxtLink></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">O Desafio</a></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Como Funciona</a></li>
            <li><a href="#" class="hover:text-indigo-400 transition-colors">Planos e Preços</a></li>
          </ul>
        </div>
        
        <div>
          <h4 class="text-sm font-black text-white uppercase tracking-widest mb-6">Empresa</h4>
          <ul class="space-y-4 text-sm text-slate-400 font-medium">
            <li><NuxtLink to="/sobre" class="hover:text-indigo-400 transition-colors">Sobre Nós</NuxtLink></li>
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
        <p class="text-sm text-slate-500 font-medium">&copy; {{ new Date().getFullYear() }} PneumoAssist. Todos os direitos reservados.</p>
        <div class="flex items-center gap-2 text-sm font-medium text-slate-500">
          Criado com rigor clínico e <i class="fas fa-heart text-rose-500 animate-pulse"></i>
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

useHead({
  title: 'Manifesto & Equipe | PneumoAssist',
  meta: [
    { name: 'description', content: 'Conheça o processo de engenharia, a stack tecnológica e a equipa por trás do PneumoAssist.' }
  ],
  link: [
    { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' }
  ]
})

// --- LÓGICA DO NAVBAR ---
const showNavbar = ref(true);
const isScrolled = ref(false);

const handleScroll = () => {
  if (typeof window === 'undefined') return;
  
  const currentScrollPosition = window.scrollY;
  isScrolled.value = currentScrollPosition > 50;

  const totalHeight = document.documentElement.scrollHeight;
  const viewportHeight = window.innerHeight;
  const scrollFromTop = window.scrollY;
  
  const distanceFromBottom = totalHeight - (scrollFromTop + viewportHeight);
  
  if (distanceFromBottom < 400) { 
    showNavbar.value = false;
  } else {
    showNavbar.value = true;
  }
};

// --- DADOS DINÂMICOS ---
const stats = [
  { num: '+3 Milhões', text: 'Mortes anuais globais causadas por infeções do trato respiratório inferior, a causa infecciosa mais letal.' },
  { num: 'Até 48h', text: 'Tempo médio de espera por um laudo radiológico oficial em sistemas de saúde públicos sobrecarregados.' },
  { num: '< 2 Seg.', text: 'Tempo que a nossa infraestrutura demora a processar um RX e gerar uma análise estruturada baseada em IA.' },
  { num: '99.9%', text: 'O nosso objetivo de SLA de disponibilidade da API, garantindo triagem contínua para urgências.' }
]

const timeline = [
  { ano: '2024', titulo: 'Identificação do Problema', desc: 'Análise profunda dos gargalos em hospitais portugueses e internacionais, percebendo que radiografias de tórax eram o exame mais comum e com maior tempo de espera.' },
  { ano: '2025', titulo: 'Desenvolvimento do Motor IA', desc: 'Integração do Llama Vision com a arquitetura Groq LPU, conseguindo reduzir os custos computacionais e o tempo de inferência de minutos para milissegundos.' },
  { ano: '2026', titulo: 'O Laboratório Clínico', desc: 'Lançamento do PneumoAssist V1. Um ambiente restrito para médicos validarem as interpretações radiológicas geradas pela inteligência artificial.' }
]

const techStack = ['Vue 3', 'Nuxt.js', 'Tailwind CSS', 'Python', 'FastAPI', 'Groq LPU', 'Llama 3.2 Vision', 'REST APIs', 'Docker']

const metricas = [
  { label: 'Model Accuracy', valor: '94.2%' },
  { label: 'Inference Time', valor: '< 2s' },
  { label: 'Data Security', valor: 'Zero Trust' },
  { label: 'Uptime (API)', valor: '99.9%' }
]

const processos = [
  { step: '01', titulo: 'Data Extraction', desc: 'O frontend envia as imagens radiológicas de forma otimizada via Base64 para a API Python segura e encriptada.' },
  { step: '02', titulo: 'Vision Inference', desc: 'O modelo Llama Vision varre o contraste de píxeis em busca de anomalias radiopacas (consolidações).' },
  { step: '03', titulo: 'Clinical Output', desc: 'A IA estrutura os achados e sintomas reportados numa formatação médica clara usando Markdown estrito.' }
]

const equipa = [
  { 
    nome: 'Miguel Massane', 
    cargo: 'Tech Lead & Frontend', 
    bio: 'Especialista em Vue/Nuxt. Responsável por arquitetar a aplicação cliente e orquestrar as animações assíncronas do chat.',
    foto: 'https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Laptop.png',
    icone: 'fas fa-code', 
    corCorpo: 'bg-indigo-600',
    github: '#', linkedin: '#' 
  },
  { 
    nome: 'Murilo Almeida De Oliveira', 
    cargo: 'Backend & Python', 
    bio: 'Construiu a ponte entre a UI e os LLMs através da FastAPI, garantindo regras rígidas de restrição de domínio.',
    foto: 'https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Cloud/3D/cloud_3d.png',
    icone: 'fas fa-server', 
    corCorpo: 'bg-blue-500',
    github: '#', linkedin: '#' 
  },
  { 
    nome: 'Joel João De Araujo Neto', 
    cargo: 'AI Engineer', 
    bio: 'Desenvolvedor do Prompt, implementou Zero Data Retention e fez o tuning fino do Llama Vision para uso pulmonar.',
    foto: 'https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Robot/3D/robot_3d.png',
    icone: 'fas fa-brain', 
    corCorpo: 'bg-emerald-500',
    github: '#', linkedin: '#' 
  },
  { 
    nome: 'Júlio Sena', 
    cargo: 'UI/UX & Design', 
    bio: 'Focou na acessibilidade. Criou o "Dark Mode" clínico e os leitores de markdown focados em dados de saúde.',
    foto: 'https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Artist%20palette/3D/artist_palette_3d.png',
    icone: 'fas fa-pen-nib', 
    corCorpo: 'bg-rose-500',
    github: '#', linkedin: '#' 
  }
]

// --- LÓGICA DE ANIMAÇÃO AO FAZER SCROLL ---
let observer: IntersectionObserver | null = null;

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true });

  observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

  document.querySelectorAll('.animate-reveal').forEach(el => {
    observer!.observe(el);
  });
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
  if (observer) observer.disconnect();
});
</script>

<style scoped>
/* ==========================================
   ANIMAÇÕES DE ENTRADA E UTILITÁRIOS
   ========================================== */
.animate-reveal {
  opacity: 0;
  will-change: transform, opacity;
  transition: opacity 0.8s ease-out, transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.reveal-up { transform: translateY(40px); }
.reveal-left { transform: translateX(-40px); }
.reveal-right { transform: translateX(40px); }
.reveal-zoom { transform: scale(0.92); }

.animate-reveal.is-visible {
  opacity: 1 !important;
  transform: translate(0) scale(1) !important;
}

/* Animação Contínua "Float" */
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-15px); }
  100% { transform: translateY(0px); }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
  will-change: transform;
}

/* Animação "Scan" */
.animate-scan {
  animation: scan 3s linear infinite;
}
@keyframes scan {
  0% { transform: translateY(0); opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { transform: translateY(300px); opacity: 0; }
}

/* Animação de Gradiente no Texto */
.animate-gradient {
  background-size: 300%;
  animation: textGradient 6s ease infinite;
}
@keyframes textGradient {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;  
  overflow: hidden;
}
</style>