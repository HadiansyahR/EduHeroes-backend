from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.answers import Answer
from models.questions import Question

def create_answer(
    db: Session,
    question_id: int,
    answer_text: str,
    is_correct: bool,
    user_id: int
):

    question = db.query(Question).filter(
        Question.id_question == question_id
    ).first()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    quiz = question.quiz

    if quiz.created_by != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed to add answers"
        )

    answer = Answer(
        question_id=question_id,
        answer_text=answer_text,
        is_correct=is_correct
    )

    db.add(answer)
    db.commit()
    db.refresh(answer)

    return answer