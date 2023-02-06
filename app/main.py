from fastapi import FastAPI

from app.routers import account, auth, policy

app = FastAPI(title="Book& 더미 REST API 문서")

app.include_router(auth.router)
app.include_router(policy.router)
app.include_router(account.router)


@app.get("/", include_in_schema=False)
async def root():
    return "Bookand Mock Up Server"
