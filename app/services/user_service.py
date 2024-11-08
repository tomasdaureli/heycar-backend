import os
from sqlalchemy.orm import Session
from schemas.badges_schema import BadgeResponse
from models.badges_model import Badge
from models.user_model import User
from schemas.user_schema import CreateUserRequest
from config.auth import encryption_context

from dotenv import load_dotenv

load_dotenv()
BADGES_LEVEL_1_POINTS = os.getenv("BADGES_LEVEL_1_POINTS")
BADGES_LEVEL_2_POINTS = os.getenv("BADGES_LEVEL_2_POINTS")
BADGES_LEVEL_3_POINTS = os.getenv("BADGES_LEVEL_3_POINTS")
BADGES_LEVEL_4_POINTS = os.getenv("BADGES_LEVEL_4_POINTS")
BADGES_LEVEL_5_POINTS = os.getenv("BADGES_LEVEL_5_POINTS")


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

    def get_user_points(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        return user.points if user else 0

    def get_user_levels(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        return user.level if user else 1

    def assign_badge(
        self, user_id: int, badge_name: str, description: str = None, score: int = 0
    ):
        badge = (
            self.db.query(Badge)
            .filter(Badge.user_id == user_id, Badge.name == badge_name)
            .first()
        )
        if badge:
            badge.description = description if description else badge.description
            badge.score = score if score else badge.score
        else:
            badge = Badge(
                user_id=user_id,
                name=badge_name,
                description=description
                or f"Otorgado por realizar la acción {badge_name}",
                score=score,
            )
            self.db.add(badge)

        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            user.points += score
            self.db.commit()
            self.db.refresh(user)
            self.update_user_level(user)

        self.db.commit()
        self.db.refresh(badge)
        return badge

    def get_user_badges(self, user_id: int):
        badges = self.db.query(Badge).filter(Badge.user_id == user_id).all()
        badge_dicts = [badge.__dict__ for badge in badges]
        return [BadgeResponse.model_validate(badge_dict) for badge_dict in badge_dicts]

    def update_user_level(self, user: User):
        if user.points >= BADGES_LEVEL_5_POINTS:
            user.level = 5
        elif user.points >= BADGES_LEVEL_4_POINTS:
            user.level = 4
        elif user.points >= BADGES_LEVEL_3_POINTS:
            user.level = 3
        elif user.points >= BADGES_LEVEL_2_POINTS:
            user.level = 2
        else:
            user.level = 1
        self.db.commit()
        self.db.refresh(user)

    def save_notification_token(self, user_id: int, token: str, type: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            user.notification_token = token
            user.notification_type = type
            self.db.commit()
            self.db.refresh(user)
            return user
        return None
