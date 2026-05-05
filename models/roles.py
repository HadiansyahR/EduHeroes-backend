from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database import Base

class Role(Base):
    __tablename__ = "roles"

    id_role: Mapped[int] = mapped_column(primary_key=True)
    role_name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    users: Mapped[list["User"]] = relationship("User", back_populates="role", cascade="all, delete")