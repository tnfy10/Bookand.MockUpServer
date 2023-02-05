from pydantic import BaseModel


class Result(BaseModel):
    result: str

    def __init__(self, result: str):
        super().__init__(result=result)
