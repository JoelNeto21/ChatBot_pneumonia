# 🫁 PneumoAssist — Inteligência Clínica Especializada

[![Nuxt](https://img.shields.io/badge/Nuxt-3.x-emerald.svg?style=flat-square&logo=nuxt.js)](https://nuxt.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.x-blue.svg?style=flat-square&logo=tailwind-css)](https://tailwindcss.com/)
[![Groq LPU](https://img.shields.io/badge/AI-Groq%20LPU-orange.svg?style=flat-square)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

> **PneumoAssist** é uma plataforma SaaS de suporte à decisão clínica focada na saúde respiratória. Utilizando visão computacional avançada e modelos de linguagem de larga escala (LLMs), o sistema auxilia na triagem de sintomas e interpretação de exames de imagem.

---

## ✨ Funcionalidades Principais

* **🔍 Análise Vision (Llama 3.2):** Interpretação instantânea de imagens de Raio-X e tomografias para identificação de padrões patológicos.
* **💬 Chatbot Clínico Contextual:** Triagem baseada em sintomas (tosse, dispneia, dor torácica) com linguagem acessível e precisa.
* **⚡ Performance Groq LPU:** Inferência ultra-rápida (menos de 15s) para diagnósticos que não podem esperar.
* **🛡️ Privacy First:** Anonimização de dados e conformidade com diretrizes inspiradas na HIPAA e GDPR.
* **🌓 Modo Escuro Nativo:** Interface otimizada para ambientes hospitalares e de baixa luminosidade.

## 🛠️ Stack Tecnológica

* **Framework:** [Nuxt 3](https://nuxt.com/) (Vue.js)
* **Estilização:** [Tailwind CSS](https://tailwindcss.com/)
* **Modelos de IA:** Llama 3.2 Vision via **Groq Cloud**
* **Ícones:** FontAwesome 6 (Pro-style)
* **Tipografia:** Plus Jakarta Sans & Montserrat

## 📂 Estrutura do Repositório

```text
├── components/          # Componentes UI (Sidebar, Chat, Cards)
├── layouts/             # Templates de página (Default, App)
├── pages/               # Rotas (Landing Page, Dashboard de Chat)
├── public/              # Ativos estáticos e ícones
├── assets/              # CSS global e Tailwind config
├── .env.example         # Exemplo de chaves de API necessárias
└── nuxt.config.ts       # Configuração do ecossistema Nuxt