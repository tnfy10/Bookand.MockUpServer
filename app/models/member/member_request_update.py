from pydantic import BaseModel


class MemberRequestUpdate(BaseModel):
    nickname: str

    def __init__(self, nickname: str):
        super().__init__(nickname=nickname)
