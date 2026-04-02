<div align="center">
  
  <img src="https://images.unsplash.com/photo-1519003300449-424ad0405076?q=80&w=698&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Banner PneumoAssist" width="100%" style="border-radius: 12px; margin-bottom: 20px; object-fit: cover; height: 250px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">

  # 🫁 PneumoAssist
  **Plataforma de Inteligência Clínica para Triagem Respiratória**

  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Plus+Jakarta+Sans&weight=600&size=20&duration=3000&pause=1000&color=10B981&center=true&vCenter=true&width=800&lines=An%C3%A1lise+radiol%C3%B3gica+com+Llama+3.2+Vision.;Triagem+inteligente+de+sintomas.;Infer%C3%AAncia+ultra-r%C3%A1pida+via+Groq+LPU.;Seguran%C3%A7a+e+anonimiza%C3%A7%C3%A3o+de+dados." alt="Typing SVG" />
  </a>

  <br>

  [![Nuxt](https://img.shields.io/badge/Nuxt-3.x-00DC82.svg?style=for-the-badge&logo=nuxt.js&logoColor=black)](https://nuxt.com/)
  [![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.x-38B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
  [![Groq LPU](https://img.shields.io/badge/AI-Groq%20LPU-F55036.svg?style=for-the-badge)](https://groq.com/)

</div>

<br>

> Em cenários de pronto-atendimento, a superlotação e a urgência exigem decisões rápidas. O **PneumoAssist** é um SaaS focado em atuar como um "co-piloto" médico, processando imagens torácicas e relatando sintomas em frações de segundo para adiantar o panorama clínico antes mesmo do contato físico com o paciente.

---

## 🚀 O Problema e a Solução

A triagem tradicional de patologias respiratórias muitas vezes depende de processos manuais e aguardo em filas de radiologia. 

Nossa solução integra **Visão Computacional** e **Modelos de Linguagem (LLMs)** operando nos processadores LPU da Groq (focados em latência zero). O sistema permite que exames de Raio-X sejam pré-avaliados instantaneamente, destacando anomalias como opacidades ou derrames pleurais, além de conduzir uma anamnese prévia via chatbot.

---

## ⚙️ Arquitetura e Fluxo de Dados

O projeto adota uma arquitetura em camadas focada em alta disponibilidade e segurança:

1. **Client (Nuxt 3):** Interface web responsiva onde o médico ou enfermeiro faz o upload do exame (DICOM/JPEG) ou insere as queixas do paciente.
2. **Processamento (Edge/Serverless):** A API do Nuxt anonimiza os dados (remove identificadores pessoais do paciente) antes do envio.
3. **Motor Cognitivo (Groq Cloud):** O modelo `Llama 3.2 Vision` interpreta a imagem e o contexto textual, retornando um JSON estruturado com os achados clínicos.
4. **Apresentação:** Os dados retornam à interface em menos de 15 segundos, formatados em um laudo preliminar amigável com alertas de gravidade (Triage Score).

---

## ✨ Funcionalidades Core

* 🔍 **Smart Vision:** Detecção de padrões pulmonares atípicos em imagens bidimensionais.
* 💬 **Anamnese AI:** Chatbot que correlaciona febre, dispneia e histórico prévio para sugerir hipóteses diagnósticas (Diferenciais).
* 🛡️ **Privacy Shield:** Sistema desenhado sob princípios de conformidade com LGPD/GDPR — nenhuma imagem enviada retém metadados do paciente.
* 🌓 **Hospital Mode:** UI ergonômica com "Modo Escuro" estrito para ambientes de baixa luminosidade, reduzindo fadiga visual da equipe médica.

---

## 🛠️ Stack Tecnológica

| Categoria | Tecnologia | Propósito no Projeto |
| :--- | :--- | :--- |
| **Front-end** | `Nuxt 3` + `Vue.js` | Performance, roteamento nativo e renderização híbrida. |
| **Estilização** | `Tailwind CSS` | Padronização de componentes visuais ágeis. |
| **Inteligência** | `Llama 3.2 Vision` | Interpretação de multimodalidade (Texto + Imagem). |
| **Infra/Cloud** | `Groq Cloud API` | Inferência da IA com latência ultrabaixa. |

---

## 👨‍💻 Equipe de Desenvolvimento

Projeto desenvolvido por uma equipe multidisciplinar, unindo expertise em engenharia de software e inteligência artificial:

<div align="center">

| [<img loading="lazy" src="https://images.unsplash.com/photo-1575089976121-8ed7b2a54265?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" width=100 style="border-radius: 50%"><br><sub><b>MIGUEL MASSANE</b></sub>](https://github.com/) | [<img loading="lazy" src="https://images.unsplash.com/photo-1629904853893-c2c8981a1dc5?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" width=100 style="border-radius: 50%"><br><sub><b>MURILO ALMEIDA DE OLIVEIRA</b></sub>](https://github.com/) | [<img loading="lazy" src="https://images.unsplash.com/photo-1629904853716-f0bc54eea481?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" width=100 style="border-radius: 50%"><br><sub><b>JOEL JOÃO DE ARAUJO NETO</b></sub>](https://github.com/) | [<img loading="lazy" src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" width=100 style="border-radius: 50%"><br><sub><b>JULIO SENA</b></sub>](https://github.com/) |
| :---: | :---: | :---: | :---: |
| Desenvolvedor Front-End | Engenheiro de IA | UI/UX Designer | Back-End / Dados |

</div>

> **Nota:** *Para editar a equipe, basta alterar os nomes no link `name=Nome+Um` para gerar as iniciais automáticas, trocar a função logo abaixo e inserir o link do LinkedIn/GitHub dentro dos parênteses `(https://...)`.*

---

## 🚀 Executando o Projeto

**1. Clone o repositório:**
```bash
git clone [https://github.com/seu-usuario/pneumoassist.git](https://github.com/seu-usuario/pneumoassist.git)
cd pneumoassist
