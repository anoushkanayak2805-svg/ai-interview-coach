from sqlalchemy.orm import Session

from app.models.answer import InterviewAnswer


def save_answer(
    db: Session,
    answer: InterviewAnswer
):
    db.add(answer)
    db.commit()
    db.refresh(answer)

    return answer