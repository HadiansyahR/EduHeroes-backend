from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from core.auth import teacher_required
from models.answers import Answer
from schemas.answer import AnswerCreate, AnswerRead
from services.answer_service import create_answer

router = APIRouter(prefix="/answers", tags=["answers"])


@router.post("/", response_model=AnswerRead)
def add_answer(
    data: AnswerCreate,
    db: Session = Depends(get_db),
    current_user = Depends(teacher_required)
):
    return create_answer(
        db,
        data.question_id,
        data.answer_text,
        data.is_correct,
        current_user.id_user
    )


@router.get("/{answer_id}", response_model=AnswerRead)
def get_answer(
    answer_id: int,
    db: Session = Depends(get_db)
):
    answer = db.query(Answer).filter(
        Answer.id_answer == answer_id
    ).first()

    if not answer:
        raise HTTPException(
            status_code=404,
            detail="Answer not found"
        )

    return answer