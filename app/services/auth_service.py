from models.user_model import User
from config.db import db_dependency
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Annotated
from config.auth import (
    access_token_expire_minutes,
    secret_key,
    algorithm,
    oauth2_bearer,
    encryption_context,
)


def authenticate_user(email: str, password: str, db: db_dependency):
    user = db.query(User).filter(User.email == email).first()
    if not user or not encryption_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return user


def create_access_token(user_id: int, user_email: str):
    to_encode = {"sub": str(user_id), "email": user_email}
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])

        email: str = payload.get("email")
        user_id: int = payload.get("sub")

        if email is None or user_id is None:
            raise HTTPException(
                status_code=401, detail="Could not validate credentials"
            )

        return {"email": email, "user_id": user_id}
    except JWTError as e:
        print(f"JWTError: {str(e)}")
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
