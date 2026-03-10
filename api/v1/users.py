from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from schemas.user import UserCreate, UserRead
from services.user_service import create_user
from core.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/me", status_code=status.HTTP_200_OK)
def get_me(current_user = Depends(get_current_user)):
    return current_user