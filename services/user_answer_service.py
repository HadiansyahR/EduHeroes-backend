from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.answers import Answer
from models.questions import Question
from models.quiz_attempts import QuizAttempt
from models.user_answers import UserAnswer


def submit_answer(
    db: Session,
    user_id: int,
    attempt_id: int,
    question_id: int,
    answer_id: int
):

    attempt = db.query(QuizAttempt).filter(
        QuizAttempt.id_attempt == attempt_id
    ).first()

    if not attempt:
        raise HTTPException(
            status_code=404,
            detail="Attempt not found"
        )

    if attempt.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not your attempt"
        )

    if attempt.is_submitted:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quiz already submitted"
        )

    question = db.query(Question).filter(
        Question.id_question == question_id
    ).first()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    answer = db.query(Answer).filter(
        Answer.id_answer == answer_id
    ).first()

    if not answer:
        raise HTTPException(
            status_code=404,
            detail="Answer not found"
        )

    if answer.question_id != question_id:
        raise HTTPException(
            status_code=400,
            detail="Answer does not belong to question"
        )

    # Prevent duplicate answer submission
    existing = db.query(UserAnswer).filter(
        UserAnswer.attempt_id == attempt_id,
        UserAnswer.question_id == question_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Question already answered"
        )

    user_answer = UserAnswer(
        attempt_id=attempt_id,
        user_id=user_id,
        question_id=question_id,
        answer_id=answer_id,
        is_correct=answer.is_correct
    )

    db.add(user_answer)
    db.commit()
    db.refresh(user_answer)

    return user_answer