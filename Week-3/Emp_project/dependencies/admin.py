from fastapi import Depends , HTTPException
from fastapi.security import OAuth2PasswordBearer
from security.user import get_current_user 
from models.model import Users


def verify_admin(current_user: Users = Depends(get_current_user)):
    if current_user.user_role != "Admin":
        raise HTTPException(status_code = 403 , detail="Admin access rejected")

    return current_user