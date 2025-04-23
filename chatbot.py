import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Carregar as variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Inicializar embeddings e carregar o vectorstore persistido
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

# Criar o modelo de linguagem
llm = OpenAI(openai_api_key=openai_api_key)

# Criar a cadeia de perguntas e respostas com base nos documentos
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

# Iniciar o loop do chat
print("Bem-vindo ao seu chatbot de TCC! Faça suas perguntas:")
while True:
    query = input("> ")
    if query.lower() in ["sair", "adeus", "fim"]:
        break

    result = qa({"query": query})
    print("Resposta:", result["result"])
    print("\n")