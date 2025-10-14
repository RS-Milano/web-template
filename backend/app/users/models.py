# Standard libraries
from datetime import datetime, UTC
# Third party libraries
from sqlalchemy import text, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, Mapped, mapped_column


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(UTC),
        nullable=False
    )
    email: Mapped[str] = mapped_column(String(254), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(60), nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r}, created_at={self.created_at!r})"
