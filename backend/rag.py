import os

from google import genai

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from config import MODEL_TYPE, GEMINI_API_KEY



# =========================
# Paths
# =========================

DB_PATH = "../data/faiss_db"

vectorstore = None



# =========================
# Gemini Client
# =========================

if MODEL_TYPE == "gemini":

    client = genai.Client(
        api_key=GEMINI_API_KEY
    )



# =========================
# Embeddings
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)



# =========================
# Process PDF
# =========================

def process_pdf(content, filename):

    global vectorstore


    os.makedirs(
        "../data",
        exist_ok=True
    )


    file_path = os.path.join(
        "../data",
        filename
    )


    with open(file_path, "wb") as f:
        f.write(content)



    loader = PyPDFLoader(
        file_path
    )


    documents = loader.load()



    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )


    chunks = splitter.split_documents(
        documents
    )



    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )


    vectorstore.save_local(
        DB_PATH
    )


    return "PDF processed and database saved"




# =========================
# Load Database
# =========================

def load_database():

    global vectorstore


    if os.path.exists(DB_PATH):

        vectorstore = FAISS.load_local(
            DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )




# =========================
# Ask Question
# =========================

def ask_question(question, history=None):

    global vectorstore



    if vectorstore is None:

        load_database()



    if vectorstore is None:

        return {
            "answer": "Please upload PDF first",
            "sources": []
        }




    # =========================
    # MMR Retrieval
    # =========================

    docs = vectorstore.max_marginal_relevance_search(
        question,
        k=6,
        fetch_k=20,
        lambda_mult=0.5
    )



    context_parts = []

    sources = []



    for doc in docs:


        page = doc.metadata.get(
            "page",
            "unknown"
        )


        source = (
            f"Page {page + 1}"
            if page != "unknown"
            else "Unknown page"
        )


        sources.append(
            source
        )


        context_parts.append(
            f"""
[Source: {source}]

{doc.page_content}
"""
        )



    context = "\n\n".join(
        context_parts
    )



    context = context[:12000]



    # =========================
    # Prompt
    # =========================

    prompt = f"""
You are an AI assistant that answers questions from a document.

Use ONLY the provided context.

Rules:
- Answer clearly and completely.
- Use numbered points when appropriate.
- Explain each point briefly.
- Include source pages when possible.
- Do not invent information.
- If the answer is not available in the document, say:
"The information is not available in the document."


Previous conversation:

{history}


Document context:

{context}


Question:

{question}


Answer:
"""



    # =========================
    # Gemini Generation
    # =========================

    if MODEL_TYPE == "gemini":

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )


        answer = response.text



    else:

        answer = "Local model is not configured yet."




    return {

        "answer": answer,

        "sources": list(set(sources))

    }