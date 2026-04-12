from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from openai import OpenAI
import uvicorn

# ==========================================
# CONFIGURAÇÕES DE IA
# ==========================================
# Modelo de Visão para análise de imagens
VISION_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
# Modelo de Texto para conversação
TEXT_MODEL = "llama-3.3-70b-versatile"
# Chave de API Groq
API_KEY = ""
# ==========================================

app = FastAPI()

# Configuração de CORS para permitir que o seu Frontend (Nuxt/Vue) comunique com o Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=API_KEY
)

class ChatRequest(BaseModel):
    message: str
    image: Optional[str] = None 

@app.post("/chat")
async def chat_with_ai(request: ChatRequest):
    try:
        # Seleciona o modelo com base na presença de imagem
        model_to_use = VISION_MODEL if request.image else TEXT_MODEL
        
        # PROMPT DE SISTEMA: Restrição total a Pneumonia e Formatação Avançada
        system_prompt = (
            "És o PneumoAssist, um assistente médico de IA especializado EXCLUSIVAMENTE em Pneumonia e patologias do trato respiratório inferior.\n\n"
            "DIRETRIZES DE RESTRIÇÃO (CRÍTICO):\n"
            "1. Só podes responder a perguntas sobre: Pneumonia, anatomia pulmonar, sintomas respiratórios e análise de exames de imagem do tórax.\n"
            "2. Se o utilizador perguntar sobre culinária, política, desporto, programação, ou qualquer tema não médico/pneumológico, deves recusar educadamente.\n"
            "3. Resposta padrão para temas proibidos: 'Lamento, mas como especialista em Pneumonia, apenas posso fornecer informações e análises relacionadas com saúde pulmonar e pneumonia.'\n\n"
            "DIRETRIZES DE ESTILO E ESCRITA (VISUAL):\n"
            "- Responde em Português (PT-PT) de forma profissional e estruturada.\n"
            "- TÍTULOS: Usa '##' para seções principais e escreve o título em MAIÚSCULAS (ex: ## ANÁLISE CLÍNICA).\n"
            "- TABELAS: Sempre que houver comparação de dados, valores de exames ou listas de sintomas, utiliza obrigatoriamente TABELAS Markdown para facilitar a leitura.\n"
            "- DESTAQUES: Usa negrito (**texto**) para termos médicos cruciais, diagnósticos ou achados importantes.\n"
            "- LISTAS: Utiliza tópicos (bullet points) para organizar recomendações ou sintomas.\n\n"
            "DIRETRIZES MÉDICAS:\n"
            "- Identifica opacidades, consolidações ou infiltrados se houver imagem.\n"
            "- NUNCA tentes gerar ou inserir links de imagens no texto.\n"
            "- REGRA DE OURO: Termina sempre com: '\n\n---\n**Nota:** Esta análise baseada em IA é uma ferramenta de apoio e não substitui de forma alguma o diagnóstico de um médico especialista.'"
        )

        # Montagem do conteúdo da mensagem
        if request.image:
            user_content = [
                {
                    "type": "text", 
                    "text": request.message if request.message else "Analisa este exame e verifica se existem sinais compatíveis com pneumonia."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": request.image
                    }
                }
            ]
        else:
            user_content = request.message

        # Chamada à API da Groq
        response = client.chat.completions.create(
            model=model_to_use,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            temperature=0.1, # Temperatura baixa para garantir que a IA não saia do tema
            max_tokens=1200
        )
        
        return {"reply": response.choices[0].message.content}
    
    except Exception as e:
        print(f"Erro Crítico na API: {str(e)}")
        return {"reply": "Lamento, ocorreu um erro ao processar a análise clínica. Por favor, tente novamente mais tarde. 🩺"}

# Execução do servidor
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)