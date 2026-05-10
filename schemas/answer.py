from pydantic import BaseModel


class AnswerCreate(BaseModel):
    question_id: int
    answer_text: str
    is_correct: bool = False


class AnswerRead(BaseModel):
    id_answer: int
    question_id: int
    answer_text: str

    class Config:
        from_attributes = True