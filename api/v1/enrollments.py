from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from core.auth import get_current_user
from schemas.enrollment import EnrollmentCreate, EnrollmentRead
from services.enrollment_service import enroll_user
from models.enrollments import Enrollment

router = APIRouter(prefix="/enrollments", tags=["enrollments"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=EnrollmentRead)
def enroll(
    data: EnrollmentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return enroll_user(db, current_user.id_user, data.course_id)

@router.get("/my", response_model=list[EnrollmentRead])
def get_my_enrollments(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Enrollment).filter(Enrollment.user_id == current_user.id_user).all()
