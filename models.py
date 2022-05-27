import time

from pydantic import BaseModel


class TaskMetaInfo(BaseModel):
    create_timestamp: int = int(time.time() * 1000)
    delay_timestamp: int
