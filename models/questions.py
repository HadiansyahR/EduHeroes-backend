from datetime import datetime
from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Question(Base):
    __tablename__ = "questions"

    id_question: Mapped[int] = mapped_column(primary_key=True)

    quiz_id: Mapped[int] = mapped_column(ForeignKey("quizzes.id_quiz"), nullable=False)
    quiz: Mapped["Quiz"] = relationship("Quiz", back_populates="questions")

    question_text: Mapped[str] = mapped_column(String, nullable=False)
    question_type: Mapped[str] = mapped_column(String, nullable=False)
    media_url: Mapped[str | None] = mapped_column(String, nullable=True)

    answers: Mapped[list["Answer"]] = relationship("Answer", back_populates="question", cascade="all, delete")
    user_answers: Mapped[list["UserAnswer"]] = relationship("UserAnswer", cascade="all, delete")

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
