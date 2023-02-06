from pydantic import BaseModel


class PolicyModel(BaseModel):
    context: str
    createdAt: str
    modifiedAt: str
    title: str
