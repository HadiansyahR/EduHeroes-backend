from datetime import datetime

from sqlalchemy import (
    Integer,
    Float,
    ForeignKey,
    DateTime,
    func
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from database import Base


class QuizResult(Base):
    __tablename__ = "quiz_results"

    id_result: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id_user"), nullable=False)
    user: Mapped["User"] = relationship("User",  foreign_keys=[user_id], back_populates="quiz_results")

    quiz_id: Mapped[int] = mapped_column(ForeignKey("quizzes.id_quiz"), nullable=False)
    quiz: Mapped["Quiz"] = relationship("Quiz", foreign_keys=[quiz_id], back_populates="quiz_results")

    total_questions: Mapped[int] = mapped_column(Integer, nullable=False)
    correct_answers: Mapped[int] = mapped_column(Integer, nullable=False)
    score: Mapped[float] = mapped_column(Float, nullable=False)

    submitted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    attempt_id: Mapped[int] = mapped_column(ForeignKey("quiz_attempts.id_attempt"), nullable=False)
    attempt: Mapped["QuizAttempt"] = relationship("QuizAttempt", foreign_keys=[attempt_id], back_populates="quiz_attempts")