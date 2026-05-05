from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from core.auth import teacher_required, get_current_user
from schemas.quiz import QuizCreate, QuizRead
from services.quiz_service import create_quiz
from models.quizzes import Quiz
from models.courses import Course

router = APIRouter(prefix="/quizzes", tags=["quizzes"])


@router.post("/", response_model=QuizRead)
def add_quiz(
    data: QuizCreate,
    db: Session = Depends(get_db),
    current_user = Depends(teacher_required)
):
    course = db.query(Course).filter(Course.id_course == data.course_id).first()

    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return create_quiz(db, data.title, data.course_id, current_user.id_user)


@router.get("/{quiz_id}", status_code=status.HTTP_200_OK, response_model=QuizRead)
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    return db.query(Quiz).filter(Quiz.id_quiz == quiz_id).first()