from fastapi import FastAPI

from app.routers import account, auth, policy

app = FastAPI(title="Book& 더미 REST API 문서")

api_v1_prefix = "/api/v1"
app.include_router(auth.router, prefix=f"{api_v1_prefix}/auth")
app.include_router(policy.router, prefix=f"{api_v1_prefix}/policy")
app.include_router(account.router, prefix=f"{api_v1_prefix}/account")


@app.get("/", include_in_schema=False)
async def root():
    return "Bookand Mock Up Server"
