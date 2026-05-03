from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.courses import Course
from models.enrollments import Enrollment
from models.users import User


def enroll_user(db: Session, user_id: int, course_id: int):

    existing = db.query(Enrollment).filter(
        Enrollment.user_id == user_id,
        Enrollment.course_id == course_id
    ).first()

    course = db.query(Course).filter(Course.id_course == course_id).first()

    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    if user_id == course.created_by:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can't enroll in your own course")
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already enrolled"
        )

    enrollment = Enrollment(
        user_id=user_id,
        course_id=course_id
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment