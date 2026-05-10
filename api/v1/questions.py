from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from core.auth import teacher_required
from models.questions import Question
from schemas.question import QuestionCreate, QuestionRead
from schemas.answer import AnswerRead
from services.question_service import create_question

router = APIRouter(prefix="/questions", tags=["questions"])


@router.post("/", response_model=QuestionRead)
def add_question(
    data: QuestionCreate,
    db: Session = Depends(get_db),
    current_user = Depends(teacher_required)
):
    return create_question(
        db,
        data.quiz_id,
        data.question_text,
        data.question_type,
        data.media_url,
        current_user.id_user
    )


@router.get("/{question_id}", response_model=QuestionRead)
def get_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    question = db.query(Question).filter(
        Question.id_question == question_id
    ).first()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    return question

@router.get("/{question_id}/answers", response_model=list[AnswerRead])
def get_question_answers(
    question_id: int,
    db: Session = Depends(get_db)
):
    question = db.query(Question).filter(
        Question.id_question == question_id
    ).first()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    return question.answers