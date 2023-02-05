from pydantic import BaseModel


class MemberRequestUpdate(BaseModel):
    nickname: str
