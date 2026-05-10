from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from core.auth import teacher_required, get_current_user
from schemas.quiz import QuizCreate, QuizRead
from schemas.question import QuestionRead
from services.quiz_service import create_quiz
from models.quizzes import Quiz

router = APIRouter(prefix="/quizzes", tags=["quizzes"])


@router.post("/", response_model=QuizRead)
def add_quiz(
    data: QuizCreate,
    db: Session = Depends(get_db),
    current_user = Depends(teacher_required)
):
    return create_quiz(db, data.title, data.course_id, current_user.id_user)


@router.get("/{quiz_id}", status_code=status.HTTP_200_OK, response_model=QuizRead)
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    return db.query(Quiz).filter(Quiz.id_quiz == quiz_id).first()

@router.get("/{quiz_id}/questions", response_model=list[QuestionRead])
def get_quiz_questions(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter(
        Quiz.id_quiz == quiz_id
    ).first()

    if not quiz:
        raise HTTPException(
            status_code=404,
            detail="Quiz not found"
        )

    return quiz.questions