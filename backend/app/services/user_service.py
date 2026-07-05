from sqlalchemy.orm import Session

from app.repositories.user_repository import update_user


def update_profile(
    db: Session,
    user,
    full_name: str
):
    user.full_name = full_name

    return update_user(
        db,
        user
    )