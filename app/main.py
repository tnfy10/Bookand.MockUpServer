from fastapi import FastAPI

from app.routers import account, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(account.router)


@app.get("/", include_in_schema=False)
async def root():
    return "Bookand Mock Up Server"