from datetime import datetime
from sqlalchemy import String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.roles import Role


class User(Base):
    __tablename__ = "users"
    id_user: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id_role"), nullable=False)
    role: Mapped["Role"] = relationship("Role", foreign_keys=[role_id], back_populates="users")

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

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

    courses: Mapped[list["Course"]] = relationship("Course", back_populates="teacher", cascade="all, delete")
    enrollments: Mapped[list["Enrollment"]] = relationship("Enrollment", back_populates="student", cascade="all, delete")
    quizzes: Mapped[list["Quiz"]] = relationship("Quiz", back_populates="creator", cascade="all, delete")
