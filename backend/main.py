from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from rag import process_pdf, ask_question

from vision import analyze_image

from database import (
    create_tables,
    save_message,
    get_messages,
    get_all_sessions
)



app = FastAPI(
    title="RAGenius AI API",
    version="1.0"
)



create_tables()



class Question(BaseModel):

    question: str
    session_id: str = "default"





@app.get("/")
def home():

    return {
        "message": "RAGenius AI is running"
    }






# =========================
# PDF Upload
# =========================

@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):


    if not file.filename.endswith(".pdf"):

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )



    content = await file.read()



    result = process_pdf(
        content,
        file.filename
    )


    return {

        "status": result

    }







# =========================
# Ask RAG
# =========================

@app.post("/ask")
def ask(data: Question):


    history = get_messages(
        data.session_id
    )



    answer = ask_question(
        data.question,
        history
    )



    save_message(
        data.session_id,
        "user",
        data.question
    )


    save_message(
        data.session_id,
        "assistant",
        answer["answer"]
    )



    return {

        "answer": answer,

        "history":
        get_messages(
            data.session_id
        )

    }







# =========================
# Image Analysis
# =========================

@app.post("/vision")
async def vision(
    file: UploadFile = File(...),
    prompt: str = "Analyze this image"
):


    image_bytes = await file.read()


    answer = analyze_image(
        image_bytes,
        prompt
    )


    return {

        "answer": answer

    }







# =========================
# History
# =========================

@app.get("/history/{session_id}")
def history(session_id: str):


    return {

        "messages":
        get_messages(session_id)

    }







# =========================
# Sessions
# =========================

@app.get("/sessions")
def sessions():

    return {

        "sessions":
        get_all_sessions()

    }