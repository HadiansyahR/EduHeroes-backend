from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.questions import Question
from models.quizzes import Quiz


def create_question(
    db: Session,
    quiz_id: int,
    question_text: str,
    question_type: str,
    media_url: str | None,
    user_id: int
):

    quiz = db.query(Quiz).filter(
        Quiz.id_quiz == quiz_id
    ).first()

    if not quiz:
        raise HTTPException(
            status_code=404,
            detail="Quiz not found"
        )

    if quiz.created_by != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to add question to this quiz"
        )

    question = Question(
        quiz_id=quiz_id,
        question_text=question_text,
        question_type=question_type,
        media_url=media_url
    )

    db.add(question)
    db.commit()
    db.refresh(question)

    return question