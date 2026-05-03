from datetime import datetime
from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

class Course(Base):
    __tablename__ = "courses"

    id_course: Mapped[int] = mapped_column(primary_key=True)

    course_name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    created_by: Mapped[int] = mapped_column(ForeignKey("users.id_user"), nullable=False)
    teacher: Mapped["User"] = relationship("User", foreign_keys=[created_by], back_populates="courses")

    enrollments: Mapped[list["Enrollment"]] = relationship("Enrollment", back_populates="course", cascade="all, delete")

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
