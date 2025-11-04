from langchain_openai.chat_models import AzureChatOpenAI
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

# Inicializa o modelo do Azure OpenAI
llm = AzureChatOpenAI(
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("ENDPOINT"),
    azure_deployment=os.getenv("MODEL_DEPLOYMENT"),
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("OPENAI_API_KEY"),
    validate_base_url=False,
    seed=13,
    temperature=0.1,
    streaming=True
)

# Teste rápido
resposta = llm.invoke("Olá, Azure! Está tudo funcionando?")
print(resposta.content)
