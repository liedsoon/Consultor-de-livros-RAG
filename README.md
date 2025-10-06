# 📚 Sistema RAG com consultas Inteligentes

Aplicação Streamlit que permite **carregar arquivos PDF ou EPUB** e fazer perguntas com base no conteúdo utilizando **RAG (Retrieval-Augmented Generation)**, **FAISS** para busca semântica e o modelo **Mistral-Saba-24B via API da Groq**.

## 📎 Exemplo de uso

1. Envie um arquivo PDF ou EPUB (ex: livro, artigo, etc).
2. Após o processamento, digite uma pergunta como:
   > "Qual é o tema principal do capítulo 2?"
3. A resposta será gerada com base no conteúdo lido e indexado.

---
<div align="center">
<img src="https://github.com/user-attachments/assets/e1ca8ebc-bd55-4914-8a3d-47e3457a048d" width="1000px" />
<img src="https://github.com/user-attachments/assets/eb8365ef-5c47-435e-8140-a42f0c956426" width="1000px" />
</div>

## 🔧 Tecnologias utilizadas

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (para PDFs)
- [Unstructured](https://github.com/Unstructured-IO/unstructured) (para EPUBs)
- [Hugging Face Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [Groq API](https://console.groq.com/) com o modelo `mistral-saba-24b`

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/liedsoon/Consultor-de-livros-RAG.git
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # no Linux/Mac
venv\Scripts\activate     # no Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a chave da API Groq

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
GROQ_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Você pode obter a chave em: https://console.groq.com/

---

## ▶️ Executando a aplicação

```bash
streamlit run app.py
```

---

## 🧠 Como funciona

1. O usuário faz upload de um arquivo PDF ou EPUB.
2. O conteúdo é dividido em pequenos blocos de texto (chunks).
3. Os chunks são vetorizados usando embeddings do HuggingFace.
4. Os vetores são armazenados em um índice FAISS.
5. O usuário envia uma pergunta, que é respondida com base nos trechos mais relevantes do documento utilizando o modelo **Mistral-Saba-24B** da Groq.


