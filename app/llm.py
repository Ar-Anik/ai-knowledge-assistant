import os

from dotenv import load_dotenv
from openai import OpenAI
from google import genai


load_dotenv()


openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def create_embedding_with_openai(text):
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )

    return response.data[0].embedding


def create_embedding_with_gemini(text):
    response = gemini_client.models.embed_content(
        model="gemini-embedding-2",
        contents=text,
    )

    return response.embeddings[0].values


def generate_answer(question, context):
    prompt = f"""
        Answer the question using only the provided context.
        
        Context:
        {context}
        
        Question:
        {question}
        
        If the answer is not available in the context, say:
        "I don't know based on the provided information."
    """

    response = gemini_client.models.generate_content(
        model='gemini-3.7-flash',
        contents=prompt,
    )

    return response.text

