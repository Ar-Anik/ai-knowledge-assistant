from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class ReturnResponse(BaseModel):
    answer: str
