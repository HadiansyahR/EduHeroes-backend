from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from core.auth import get_current_user
from schemas.user_answer import UserAnswerCreate, UserAnswerRead
from services.user_answer_service import submit_answer

router = APIRouter(prefix="/user-answers", tags=["user_answers"])


@router.post("/", response_model=UserAnswerRead)
def submit_user_answer(
    data: UserAnswerCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return submit_answer(
        db,
        current_user.id_user,
        data.attempt_id,
        data.question_id,
        data.answer_id
    )