from sqlalchemy.orm import Session

from app.models.report import InterviewReport


def create_report(
    db: Session,
    report: InterviewReport,
):
    db.add(report)
    db.commit()
    db.refresh(report)
    return report


def update_report(
    db: Session,
    report: InterviewReport,
):
    db.commit()
    db.refresh(report)
    return report


def get_report_by_id(
    db: Session,
    report_id: int,
):
    return (
        db.query(InterviewReport)
        .filter(
            InterviewReport.id == report_id
        )
        .first()
    )


def get_report_by_interview(
    db: Session,
    interview_id: int,
):
    return (
        db.query(InterviewReport)
        .filter(
            InterviewReport.interview_id == interview_id
        )
        .first()
    )


def delete_report(
    db: Session,
    report: InterviewReport,
):
    db.delete(report)
    db.commit()