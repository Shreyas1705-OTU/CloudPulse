from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user,
)
from app.database.session import get_db
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    service = UserService(db)

    existing_user = service.get_user_by_username(
        user.username
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
        )

    created_user = service.create_user(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    return created_user


@router.post(
    "/login",
    response_model=Token,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    service = UserService(db)

    user = service.authenticate_user(
        form_data.username
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    if not verify_password(
        form_data.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    access_token = create_access_token(
        {
            "sub": user.username,
            "role": user.role,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user=Depends(get_current_user),
):
    return current_user