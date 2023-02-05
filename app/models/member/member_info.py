from pydantic import BaseModel


class MemberInfo(BaseModel):
    email: str
    nickname: str
    providerEmail: str

    def __init__(self, email: str, nickname: str, providerEmail: str):
        super().__init__(email=email, nickname=nickname, providerEmail=providerEmail)
