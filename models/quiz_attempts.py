from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id_attempt: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id_user"), nullable=False)
    user: Mapped["User"] = relationship("User", foreign_keys=[user_id], back_populates="quiz_attempts")

    quiz_id: Mapped[int] = mapped_column(ForeignKey("quizzes.id_quiz"), nullable=False)
    quiz: Mapped["Quiz"] = relationship("Quiz", foreign_keys=[quiz_id], back_populates="quiz_attempts")

    is_submitted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
