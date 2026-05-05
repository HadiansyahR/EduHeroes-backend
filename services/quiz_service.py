from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.quizzes import Quiz
from models.courses import Course


def create_quiz(db: Session, title: str, course_id: int, user_id: int):

    course = db.query(Course).filter(Course.id_course == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Only teacher can create quiz for their course
    if course.created_by != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed to create quiz for this course"
        )

    quiz = Quiz(
        title=title,
        course_id=course_id,
        created_by=user_id
    )

    db.add(quiz)
    db.commit()
    db.refresh(quiz)

    return quiz