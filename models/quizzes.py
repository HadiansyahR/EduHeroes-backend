from datetime import datetime
from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Quiz(Base):
    __tablename__ = "quizzes"

    id_quiz: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String, nullable=False)

    type: Mapped[str] = mapped_column(String, nullable=False)

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id_course"), nullable=False)
    course: Mapped["Course"] = relationship("Course", foreign_keys=[course_id], back_populates="quizzes")

    created_by: Mapped[int] = mapped_column(ForeignKey("users.id_user"), nullable=False)
    creator: Mapped["User"] = relationship("User", foreign_keys=[created_by], back_populates="quizzes")

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