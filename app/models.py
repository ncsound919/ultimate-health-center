from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class UserBase(SQLModel):
    email: str = Field(index=True, unique=True)
    full_name: str
    is_active: bool = True


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    role: str = Field(default="user", index=True)  # user | professional | admin
    created_at: datetime = Field(default_factory=datetime.utcnow)

    professional_profile: "ProfessionalProfile" = Relationship(back_populates="user")


class ProfessionalProfileBase(SQLModel):
    title: str
    bio: str
    specialties: str  # comma-separated list for now
    remote_only: bool = False
    location: Optional[str] = None


class ProfessionalProfile(ProfessionalProfileBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")

    user: User = Relationship(back_populates="professional_profile")


class ProgramBase(SQLModel):
    name: str
    description: str
    category: str  # e.g. "meal", "workout", "mental"
    level: str = "beginner"


class Program(ProgramBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_by_id: Optional[int] = Field(default=None, foreign_key="user.id")


class ProductBase(SQLModel):
    name: str
    description: str
    product_type: str  # e.g. "vitamin", "herbal", "equipment"
    price_cents: int
    currency: str = "usd"


class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    partner_name: Optional[str] = None
