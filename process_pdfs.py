import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Carregar as variáveis de ambiente (sua chave da OpenAI)
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Definir o diretório dos PDFs
pdf_folder_path = "inputs"

# Listar todos os arquivos PDF na pasta
pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith(".pdf")]

# Carregar os documentos PDF
documents = []
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder_path, pdf_file)
    loader = PyPDFLoader(pdf_path)
    documents.extend(loader.load())

# Dividir o texto em chunks menores
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)

# Criar embeddings dos chunks de texto
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = Chroma.from_documents(chunks, embeddings)

# Salvar o vectorstore (opcional, mas útil para não precisar recriar sempre)
vectorstore.persist()

print(f"Foram processados {len(pdf_files)} arquivos PDF e criados {len(chunks)} chunks de texto.")
print("O vectorstore foi criado e persistido.")