from fastapi import status

from app.exceptions.base import AppException


class InterviewNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )


class InterviewAccessDeniedException(AppException):

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )