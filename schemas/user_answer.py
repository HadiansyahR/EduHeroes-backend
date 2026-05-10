from pydantic import BaseModel


from pydantic import BaseModel


class UserAnswerCreate(BaseModel):
    attempt_id: int
    question_id: int
    answer_id: int


class UserAnswerRead(BaseModel):
    id_user_answer: int
    attempt_id: int
    user_id: int
    question_id: int
    answer_id: int
    is_correct: bool

    class Config:
        from_attributes = True