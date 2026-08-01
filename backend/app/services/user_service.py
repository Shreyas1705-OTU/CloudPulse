from sqlalchemy.orm import Session

from app.database.models import User


class UserService:

    def __init__(self, db: Session):
        self.db = db

    def get_user_by_username(self, username: str):
        return (
            self.db.query(User)
            .filter(User.username == username)
            .first()
        )

    def create_user(
        self,
        username: str,
        email: str,
        hashed_password: str,
        role: str = "user"
    ):
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            role=role,
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
        