from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from openai import OpenAI
import uvicorn

# ==========================================
# CONFIGURAÇÕES DE IA (Atualizado)
# ==========================================
# O modelo de Visão Estável da Groq no momento:
VISION_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
# O modelo de Texto Estável:
TEXT_MODEL = "llama-3.3-70b-versatile"
API_KEY = ""
# ==========================================

app = FastAPI()

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
        model_to_use = VISION_MODEL if request.image else TEXT_MODEL
        
        # O "Cérebro" da IA refinado e profissional
        system_prompt = (
            "És o PneumoAssist (Dra. Ana Silva), uma IA avançada especializada em pneumologia.\n"
            "O teu objetivo é analisar imagens médicas (Raio-X, TC) e responder a dúvidas clínicas de forma precisa.\n\n"
            "DIRETRIZES DE RESPOSTA:\n"
            "1. Responde em Português (PT-PT) com um tom empático, profissional e muito claro.\n"
            "2. Estrutura a tua resposta de forma limpa usando Markdown: usa **negritos** para destacar termos importantes e *bullet points* para listar anomalias ou recomendações.\n"
            "3. REGRA DE OURO: NÃO insiras links de imagens, marcadores de imagem ou tags Markdown (como ![imagem]) na tua resposta. Nunca tentes gerar imagens automaticamente.\n"
            "4. Termina sempre a análise com um breve aviso médico (ex: 'Nota: Esta análise baseada em IA não substitui a avaliação de um médico especialista.')."
        )

        if request.image:
            user_content = [
                {
                    "type": "text", 
                    "text": request.message if request.message else "Analisa esta imagem médica detalhadamente, identificando possíveis opacidades, infiltrados ou anomalias anatómicas."
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

        response = client.chat.completions.create(
            model=model_to_use,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            temperature=0.2, # Mantemos temperatura baixa para o relatório ser muito factual e não "inventar"
            max_tokens=1500
        )
        
        return {"reply": response.choices[0].message.content}
    
    except Exception as e:
        print(f"Erro Crítico na API: {str(e)}")
        return {"reply": "Lamento, ocorreu um erro de comunicação com o servidor de IA. Por favor, tente novamente. 🩺"}
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)