from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.users import User
from core.security import verify_password
from core.jwt import create_access_token

def authenticate_user(db: Session, identifier: str, password: str):
    user = db.query(User).filter(
        or_(
            User.username == identifier,
            User.email == identifier
        )
    ).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return create_access_token({"sub": str(user.id_user)})

