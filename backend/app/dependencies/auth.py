from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.config import settings
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    print("\n========== AUTH DEBUG ==========")
    print("Received Token:", token)

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        print("Decoded Payload:", payload)

        email = payload.get("sub")

        print("Email from Token:", email)

        if email is None:
            print("ERROR: Email missing from token.")
            raise credentials_exception

    except JWTError as e:
        print("JWT ERROR:", str(e))
        raise credentials_exception

    print("Searching user in database...")

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    print("Database User:", user)

    if user is None:
        print("ERROR: User not found.")
        raise credentials_exception

    print("Authentication Successful!")
    print("================================\n")

    return user