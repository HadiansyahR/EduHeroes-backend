from datetime import datetime
from pydantic import BaseModel


class QuizAttemptRead(BaseModel):
    id_attempt: int
    user_id: int
    quiz_id: int
    is_submitted: bool
    started_at: datetime
    submitted_at: datetime | None

    class Config:
        from_attributes = True