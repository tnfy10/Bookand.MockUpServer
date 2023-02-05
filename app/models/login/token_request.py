from pydantic import BaseModel


class TokenRequest(BaseModel):
    refreshToken: str
