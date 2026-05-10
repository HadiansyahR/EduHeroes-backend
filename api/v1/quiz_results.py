from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from core.auth import get_current_user
from schemas.quiz_result import QuizResultRead
from services.quiz_result_service import calculate_quiz_result

router = APIRouter(prefix="/quiz-results", tags=["quiz_results"])


@router.post("/{quiz_id}", response_model=QuizResultRead)
def generate_result(
    quiz_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return calculate_quiz_result(
        db,
        current_user.id_user,
        quiz_id
    )