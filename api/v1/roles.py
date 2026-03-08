from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from schemas.role import RoleCreate, RoleRead
from services.role_service import create_role

router = APIRouter(prefix="/roles", tags=["roles"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=RoleRead)
def add_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)