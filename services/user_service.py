from sqlalchemy.orm import Session

from models.users import User
from schemas.user import UserCreate
from core.security import hash_password

def create_user(db: Session, user: UserCreate) -> User:
    print(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password= hash_password(user.password),
        role_id=user.role_id
    )

    print(db_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user