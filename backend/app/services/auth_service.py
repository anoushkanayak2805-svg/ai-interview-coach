from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.user import User
from app.core.security import hash_password, verify_password


def create_user(db: Session, user):
    try:
        db_user = User(
            name=user.name,
            email=user.email,
            hashed_password=hash_password(user.password)
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    except SQLAlchemyError:
        db.rollback()
        raise

    except Exception:
        db.rollback()
        raise


def authenticate(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user