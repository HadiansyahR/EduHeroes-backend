from datetime import datetime
from sqlalchemy import ForeignKey, UniqueConstraint, DateTime, func, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Enrollment(Base):
    __tablename__ = "enrollments"

    id_enrollment: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id_user"), nullable=False)
    student: Mapped["User"] = relationship("User", back_populates="enrollments")

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id_course"), nullable=False)
    course: Mapped["Course"] = relationship("Course", back_populates="enrollments")

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

    __table_args__ = (
        UniqueConstraint("user_id", "course_id", name="unique_user_course"),
        Index("idx_user_course", "user_id", "course_id")
    )
