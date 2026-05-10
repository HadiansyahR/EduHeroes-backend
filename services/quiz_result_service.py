from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.quiz_attempts import QuizAttempt
from models.quiz_results import QuizResult
from models.user_answers import UserAnswer


def finalize_attempt(
    db: Session,
    user_id: int,
    attempt_id: int
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
            status_code=403,
            detail="Not your attempt"
        )

    if attempt.is_submitted:
        raise HTTPException(
            status_code=400,
            detail="Attempt already submitted"
        )

    answers = db.query(UserAnswer).filter(
        UserAnswer.attempt_id == attempt_id
    ).all()

    total_questions = len(answers)

    correct_answers = sum(
        1 for answer in answers if answer.is_correct
    )

    score = 0

    if total_questions > 0:
        score = (correct_answers / total_questions) * 100

    result = QuizResult(
        attempt_id=attempt_id,
        user_id=user_id,
        quiz_id=attempt.quiz_id,
        total_questions=total_questions,
        correct_answers=correct_answers,
        score=score
    )

    attempt.is_submitted = True
    attempt.submitted_at = datetime.utcnow()

    db.add(result)
    db.commit()
    db.refresh(result)

    return result