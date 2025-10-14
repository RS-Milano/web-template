# Standard libraries
from typing import Annotated
# Third party libraries
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import decode as jwt_decode
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
# Moduls
from backend.settings import settings
from schemas import User
from utils import users_service


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", scheme_name="JWT")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    try:
        payload = jwt_decode(token, settings.jwt.secret_key, algorithms=[settings.jwt.algorithm])
    except (InvalidTokenError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    user = users_service.get_user_by_id(payload.get("sub"))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
