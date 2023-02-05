from fastapi import FastAPI

from app.routers import account

app = FastAPI()

app.include_router(account.router)


@app.get("/", include_in_schema=False)
async def root():
    return "Bookand Mock Up Server"
