from pydantic import BaseModel


class AuthRequest(BaseModel):
    accessToken: str
    id: str
    socialType: str
