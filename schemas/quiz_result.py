from pydantic import BaseModel


class QuizResultRead(BaseModel):
    id_result: int
    user_id: int
    quiz_id: int
    total_questions: int
    correct_answers: int
    score: float

    class Config:
        from_attributes = True