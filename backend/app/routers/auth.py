from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.security import hash_password

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    service = UserService(db)

    existing_user = service.get_user_by_username(
        user.username
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    created_user = service.create_user(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    return created_user
    