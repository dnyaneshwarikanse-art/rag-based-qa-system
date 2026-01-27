from fastapi import FastAPI, UploadFile, BackgroundTasks
from app.ingest import ingest_document
from app.query import ask_question

app = FastAPI(title="RAG Based QA System")

@app.post("/upload")
async def upload_document(
    file: UploadFile,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(ingest_document, file)
    return {"message": "Document ingestion started"}

@app.post("/ask")
async def ask(query: str):
    return {"answer": ask_question(query)}
