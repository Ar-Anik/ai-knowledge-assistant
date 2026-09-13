from fastapi import FastAPI
from app.rag import load_document, chunk_text, index_document, search_similar_chunks, answer_question
from app.llm import create_embedding_with_gemini, create_embedding_with_openai


app = FastAPI()

# @app.get("/")
# def root():
#     document = load_document()
#     chunks = chunk_text(document)
#
#     return {
#         "document_length": len(document),
#         "chunk_count": len(chunks),
#         "chunks": chunks,
#     }

@app.get("/")
def root():
    vector = create_embedding_with_gemini(
        "Employees receive 20 annual leave days."
    )

    return {
        "vector_length": len(vector),
        "first_values": vector[:5],
    }


@app.post('/index')
def index():
    chunk_count = index_document()

    return {
        'message': "Document Indexed Successfully",
        'chunk_count': chunk_count
    }


@app.get('/search')
def search(question: str):
    chunks = search_similar_chunks(question)

    return {
        'question': question,
        'chunks': chunks,
    }

from .schemas import AskRequest, ReturnResponse

@app.post("/ask", response_model=ReturnResponse)
def ask(request: AskRequest):
    answer = answer_question(request.question)

    return ReturnResponse(
        answer=answer
    )
