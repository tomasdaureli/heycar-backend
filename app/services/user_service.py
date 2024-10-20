from sqlalchemy.orm import Session
from models.user_model import User
from schemas.user_schema import CreateUserRequest
from config.auth import encryption_context


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: CreateUserRequest):
        db_user = User(
            name=user.name,
            email=user.email,
            password=encryption_context.hash(user.password),
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()
