from pydantic import BaseModel


class MemberInfo(BaseModel):
    email: str
    nickname: str
    providerEmail: str
