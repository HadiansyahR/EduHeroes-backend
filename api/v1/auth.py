from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import get_db
from schemas.auth import LoginRequest, Token
from services.auth_service import authenticate_user

router = APIRouter(prefix="/auth", tags=["auth"])

# Ini dipake/uncomment kalo udah ga pake swagger buat testing
# @router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
# def login_user(data: LoginRequest, db: Session = Depends(get_db)):
#     token = authenticate_user(db, data.identifier, data.password)
#     if not token:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
#
#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }

@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = authenticate_user(db, form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return {
        "access_token": token,
        "token_type": "bearer"
    }