# Standard libraties
from datetime import datetime
from uuid import UUID
# Third party libraries
from pydantic import BaseModel

class User(BaseModel):
    id: UUID
    email: str
    created_at: datetime
