from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: int
    file_name: str

    skills: Optional[str] = None
    projects: Optional[str] = None
    analysis: Optional[str] = None

    created_at: Optional[datetime] = None

    model_config = {
        "from_attributes": True
    }