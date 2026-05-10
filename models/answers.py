from datetime import datetime
from sqlalchemy import String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Answer(Base):
    __tablename__ = "answers"

    id_answer: Mapped[int] = mapped_column(primary_key=True)

    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id_question"), nullable=False)
    question: Mapped["Question"] = relationship("Question", back_populates="answers")

    answer_text: Mapped[str] = mapped_column(String, nullable=False)
    is_correct: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

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
