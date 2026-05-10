from datetime import datetime
from sqlalchemy import Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class UserAnswer(Base):
    __tablename__ = "user_answers"

    id_user_answer: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id_user"), nullable=False)
    user: Mapped["User"] = relationship("User")

    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id_question"), nullable=False)
    question: Mapped["Question"] = relationship("Question")

    answer_id: Mapped[int] = mapped_column(ForeignKey("answers.id_answer"), nullable=False)
    answer: Mapped["Answer"] = relationship("Answer")

    is_correct: Mapped[bool] = mapped_column(Boolean, nullable=False)

    submitted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )