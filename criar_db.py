import pprint
from langchain_community.document_loaders import PyPDFDirectoryLoader

file_path = "base"

def criar_db():
    documentos = carregar_documentos()
    print("Documentos carregados com sucesso.", documentos)
    # chunks = dividir_chunks(documentos)
    # vetorizar_chunks(chunks)

def carregar_documentos():
    # Função para carregar documentos
    loader = PyPDFDirectoryLoader(file_path)
    docs = loader.load()

    pprint.pp(docs[0].metadata)
    pprint.pp(docs[0].page_content)
    
    return docs

def dividir_chunks():
    # Função para dividir documentos em chunks
    pass

def vetorizar_chunks():
    # Função para criar embeddings dos chunks
    pass

criar_db()    
pass