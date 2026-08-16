import jwt
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Users
from security import get_username_from_token , create_access_token , authenticate_user
from hash_methods import verify_hash_password , generate_hashed_password

SECRET_KEY = "my-secret-key"
ALGORITHM = "HS256"

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    username = get_username_from_token(token)

    user = (db.query(Users).filter(Users.username == username).first())

    if user is None:
        raise HTTPException(status_code=401,detail="User not found")

    return user

# def create_access_token(username: str) -> str:

#     expire = (datetime.now(timezone.utc)+ timedelta(minutes=30))

#     payload = {"sub": username,"exp": expire}

#     return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def authenticate_user(db: Session,username: str,password: str):
    user = (db.query(Users).filter(Users.username == username).first())

    if user is None:
        return None

    if not verify_hash_password(password,user.hashed_password):
        return None

    return user

def get_username_from_token(token: str) -> str:
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")
        return username

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")

