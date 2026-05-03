from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from models.users import User
from core.jwt import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="api/v1/auth/login"
)

def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_user: int = payload.get('sub')
        if id_user is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.id_user == id_user).first()

    if user is None:
        raise HTTPException(status_code=401)

    return user

def teacher_required(user = Depends(get_current_user)):
    if user.role.role_name != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only teachers can perform this action"
        )
    return user