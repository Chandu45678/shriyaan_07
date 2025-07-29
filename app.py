from fastapi import FastAPI
from retriever import retrieve_paper
from summarizer import summarize_text

app = FastAPI()

@app.post("/summarize/")
async def summarize_paper(query: str):
    retrieved_text = retrieve_paper(query)
    if retrieved_text == "No relevant paper found.":
        return {"summary": "No relevant research found."}
    
    summary = summarize_text(retrieved_text)
    return {"summary": summary}

# Run using: uvicorn app:app --reload
