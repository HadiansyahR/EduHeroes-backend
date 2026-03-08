from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from database import Base

class Role(Base):
    __tablename__ = "roles"

    id_role: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(String, unique=True, nullable=False)