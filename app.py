import os 
import streamlit as st
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain_community.document_loaders import PyMuPDFLoader, UnstructuredEPubLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI

load_dotenv()

st.set_page_config(page_title="Chat Livros", layout="wide")
st.title("📚 Consultor de livros RAG")

#1. Upload do arquivo
uploaded_file = st.file_uploader("Envie um arquivo PDF ou EPUB", type=["pdf", "epub"])

if uploaded_file:
    os.makedirs("docs", exist_ok=True)
    file_path = f"docs/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    #2. Carregamento do documento
    file_ext = os.path.splitext(uploaded_file.name)[1].lower()
    if file_ext == ".pdf":
        loader = PyMuPDFLoader(file_path)
    elif file_ext == ".epub":
        loader = UnstructuredEPubLoader(file_path)
    else:
        st.error("Formato não suportado. Envie um PDF ou EPUB.")
        st.stop()

    docs = loader.load()

    #3. Divisão em chunks
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    #4. Embeddings e índice FAISS
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    #5. Configuração do LLM (ChatOpenAI apontando para Groq + Mistral-Saba)
    llm = ChatOpenAI(
        openai_api_key=os.getenv("GROQ_API_KEY"),
        openai_api_base="https://api.groq.com/openai/v1",
        model_name="mistral-saba-24b",
        temperature=0.0
    )
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    st.success(f"{uploaded_file.name} processado com sucesso! Agora faça sua pergunta.")

    #6. Interface de perguntas
    pergunta = st.text_input("Pergunte algo sobre o documento:")
    if st.button("Enviar"):
        if pergunta.strip() == "":
            st.warning("Por favor, digite uma pergunta antes de enviar.")
        else:
            with st.spinner("Consultando Mistral-Saba via Groq..."):
                resposta = rag_chain.run(pergunta)
            st.markdown(f"**Resposta:** {resposta}")
