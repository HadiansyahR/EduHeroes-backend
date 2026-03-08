from sqlalchemy.orm import Session

from models.roles import Role
from schemas.role import RoleCreate


def create_role(db: Session, role: RoleCreate) -> Role:
    db_role = Role(
        role_name = role.role_name
    )

    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    
    return db_role