from fastapi import APIRouter

from app.dependencies import fake
from app.models.account.member_info import MemberInfo
from app.models.login.auth_request import AuthRequest
from app.models.login.login_request import LoginRequest
from app.models.login.token_request import TokenRequest
from app.models.login.token_response import TokenResponse
from app.models.common.result import Result

router = APIRouter(tags=["로그인 API"])


@router.post("/admin", name="어드민 전용")
async def post_admin_login(login_request: LoginRequest) -> TokenResponse:
    return TokenResponse(accessToken=fake.text(), refreshToken=fake.text())


@router.post("/admin/manager", name="매니저 생성")
async def post_create_manager(member_info: MemberInfo) -> Result:
    return Result(result="OK")


@router.post("/login", name="소셜 로그인")
async def post_social_login(auth_request: AuthRequest) -> TokenResponse:
    return TokenResponse(accessToken=fake.text(), refreshToken=fake.text())


@router.get("/logout", name="로그아웃")
async def get_logout() -> Result:
    return Result(result="OK")


@router.post("/manager", name="매니저 전용")
async def post_manager_login(login_request: LoginRequest) -> TokenResponse:
    return TokenResponse(accessToken=fake.text(), refreshToken=fake.text())


@router.post("/reissue", name="토큰 재발행")
async def post_reissue_token(token_request: TokenRequest) -> TokenResponse:
    return TokenResponse(accessToken=fake.text(), refreshToken=fake.text())
