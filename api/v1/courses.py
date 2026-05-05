from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.course import CourseCreate, CourseRead, CourseUpdate
from schemas.quiz import QuizRead
from services.course_service import create_course, update_course, delete_course
from core.auth import get_current_user, teacher_required
from models.courses import Course

router = APIRouter(prefix="/courses", tags=["courses"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CourseRead)
def add_course(
        course: CourseCreate,
        db: Session = Depends(get_db),
        current_user = Depends(teacher_required)
):
    return create_course(db, course, current_user.id_user)

@router.get("/", response_model=list[CourseRead])
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

@router.get("/my", response_model=list[CourseRead])
def get_my_courses(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Course).filter(Course.created_by == current_user.id_user).all()

@router.get("/{course_id}", response_model=CourseRead)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id_course == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=CourseRead)
def update_course_endpoint(
    course_id: int,
    data: CourseUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(teacher_required)
):
    course = update_course(db, course_id, data, current_user.id_user)

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return course

@router.delete("/{course_id}")
def delete_course_endpoint(
    course_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(teacher_required)
):
    success = delete_course(db, course_id, current_user.id_user)

    if not success:
        raise HTTPException(status_code=404, detail="Course not found")

    return {"message": "Course deleted"}

@router.get("/{course_id}/students")
def get_course_students(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id_course == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return [enrollment.student for enrollment in course.enrollments]

@router.get("/{course_id}/quizzes", response_model=list[QuizRead])
def get_course_quizzes(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id_course == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    return course.quizzes
