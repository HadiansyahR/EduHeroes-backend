from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.quizzes import Quiz
from models.quiz_attempts import QuizAttempt


def start_quiz_attempt(
    db: Session,
    user_id: int,
    quiz_id: int
):

    quiz = db.query(Quiz).filter(
        Quiz.id_quiz == quiz_id
    ).first()

    if not quiz:
        raise HTTPException(
            status_code=404,
            detail="Quiz not found"
        )

    # Prevent teacher from taking own quiz
    if quiz.created_by == user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You cannot take your own quiz"
        )

    attempt = QuizAttempt(
        user_id=user_id,
        quiz_id=quiz_id
    )

    db.add(attempt)
    db.commit()
    db.refresh(attempt)

    return attempt