from pydantic import BaseModel, Field


class TokenResponse(BaseModel):
    accessToken: str
    refreshToken: str
