from pydantic import BaseModel


class QuizCreate(BaseModel):
    title: str
    course_id: int
    type: str


class QuizRead(BaseModel):
    id_quiz: int
    title: str
    type: str
    course_id: int
    created_by: int

    class Config:
        from_attributes = True
