from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from models.courses import Course
from schemas.course import CourseCreate, CourseUpdate

def create_course(db: Session, course: CourseCreate, teacher_id: int):

    db_course = Course(
        course_name=course.course_name,
        description=course.description,
        created_by=teacher_id
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course

def update_course(db: Session, course_id: int, data: CourseUpdate, current_user_id: int):
    course = db.query(Course).filter(Course.id_course == course_id).first()

    if not course:
        return None
    if course.created_by != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed to modify this course"
        )
    if data.course_name is not None:
        course.course_name = data.course_name
    if data.description is not None:
        course.description = data.description

    db.commit()
    db.refresh(course)

    return course

def delete_course(db: Session, course_id: int, current_user_id: int):
    course = db.query(Course).filter(Course.id_course == course_id).first()

    if not course:
        return False
    if course.created_by != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed to delete this course"
        )

    db.delete(course)
    db.commit()

    return True