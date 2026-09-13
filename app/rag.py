from pathlib import Path
import chromadb

DOCUMENT_PATH = Path("data/company_policy.txt")

def load_document():
    return DOCUMENT_PATH.read_text(encoding="utf-8")

def chunk_text(text, chunk_size=300):
    chunks = []

    for start in range(0, len(text), chunk_size):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)

    return chunks

chroma_client = chromadb.PersistentClient(
    path='./chroma_db'
)

collection = chroma_client.get_or_create_collection(
    name='company_plolicy'
)

from .llm import create_embedding_with_gemini

def index_document():
    document = load_document()

    chunks = chunk_text(document)

    for index, chunk in enumerate(chunks):
        embedding = create_embedding_with_gemini(chunk)

        collection.upsert(
            ids=[f'chunk-{index}'],
            embeddings=[embedding],
            documents=[chunk],
        )

    return len(chunks)


def search_similar_chunks(question, top_k=2):
    question_embedding = create_embedding_with_gemini(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k,
    )

    return results['documents'][0]


from .llm import generate_answer

def answer_question(question):
    chunks = search_similar_chunks(question)

    context = '\n\n'.join(chunks)

    answer = generate_answer(
        question=question,
        context=context,
    )

    return answer


