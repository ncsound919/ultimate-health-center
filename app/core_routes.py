from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select

from .auth import get_current_user
from .database import get_session
from .models import ProfessionalProfile, ProfessionalProfileBase, Program, ProgramBase, Product, ProductBase, User


router = APIRouter(prefix="/core", tags=["core"])


class ProfessionalProfileRead(ProfessionalProfileBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class ProgramRead(ProgramBase):
    id: int

    class Config:
        from_attributes = True


class ProductRead(ProductBase):
    id: int

    class Config:
        from_attributes = True


class ProfessionalProfileCreate(ProfessionalProfileBase):
    pass


class ProgramCreate(ProgramBase):
    pass


class ProductCreate(ProductBase):
    pass


@router.post("/professionals", response_model=ProfessionalProfileRead)
async def create_professional_profile(
    profile_in: ProfessionalProfileCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.role not in {"professional", "admin"}:
        raise HTTPException(status_code=403, detail="Only professionals can create profiles")

    profile = ProfessionalProfile(**profile_in.model_dump(), user_id=current_user.id)
    session.add(profile)
    session.commit()
    session.refresh(profile)
    return profile


@router.get("/professionals", response_model=List[ProfessionalProfileRead])
async def list_professionals(
    session: Session = Depends(get_session),
    specialty: Optional[str] = None,
    remote_only: Optional[bool] = None,
):
    query = select(ProfessionalProfile)
    if specialty:
        query = query.where(ProfessionalProfile.specialties.contains(specialty))
    if remote_only is not None:
        query = query.where(ProfessionalProfile.remote_only == remote_only)
    profiles = session.exec(query).all()
    return profiles


@router.post("/programs", response_model=ProgramRead)
async def create_program(
    program_in: ProgramCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.role not in {"professional", "admin"}:
        raise HTTPException(status_code=403, detail="Only professionals can create programs")

    program = Program(**program_in.model_dump(), created_by_id=current_user.id)
    session.add(program)
    session.commit()
    session.refresh(program)
    return program


@router.get("/programs", response_model=List[ProgramRead])
async def list_programs(
    session: Session = Depends(get_session),
    category: Optional[str] = None,
    level: Optional[str] = None,
):
    query = select(Program)
    if category:
        query = query.where(Program.category == category)
    if level:
        query = query.where(Program.level == level)
    programs = session.exec(query).all()
    return programs


@router.post("/products", response_model=ProductRead)
async def create_product(
    product_in: ProductCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.role not in {"professional", "admin"}:
        raise HTTPException(status_code=403, detail="Only partners can create products")

    product = Product(**product_in.model_dump(), partner_name=current_user.full_name)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


@router.get("/products", response_model=List[ProductRead])
async def list_products(
    session: Session = Depends(get_session),
    product_type: Optional[str] = None,
):
    query = select(Product)
    if product_type:
        query = query.where(Product.product_type == product_type)
    products = session.exec(query).all()
    return products
