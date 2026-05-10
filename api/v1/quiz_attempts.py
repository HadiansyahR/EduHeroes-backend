from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from core.auth import get_current_user

from schemas.quiz_result import QuizResultRead
from services.quiz_result_service import finalize_attempt


router = APIRouter(prefix="/quiz-attempts", tags=["quiz_attempts"])

@router.post(
    "/{attempt_id}/submit",
    response_model=QuizResultRead
)
def submit_attempt(
    attempt_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return finalize_attempt(
        db,
        current_user.id_user,
        attempt_id
    )