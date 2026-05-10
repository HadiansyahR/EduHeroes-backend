from pydantic import BaseModel


class QuestionCreate(BaseModel):
    quiz_id: int
    question_text: str
    question_type: str
    media_url: str | None = None


class QuestionRead(BaseModel):
    id_question: int
    quiz_id: int
    question_text: str
    question_type: str
    media_url: str | None

    class Config:
        from_attributes = True