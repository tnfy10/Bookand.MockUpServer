from fastapi import APIRouter

from app.dependencies import fake
from app.models.account.member_info import MemberInfo
from app.models.account.member_request_update import MemberRequestUpdate
from app.models.common.result import Result

router = APIRouter(tags=["회원 API"])


@router.get("/me", name="회원 정보")
async def get_me() -> MemberInfo:
    return MemberInfo(email=fake.email(), nickname=fake.name(), providerEmail=fake.email())


@router.get("/nickname/{nickname}", name="닉네임 검증 api")
async def get_nickname_valid(nickname: str) -> bool:
    return nickname != fake.name()


@router.post("/profile", name="회원 프로필 변경")
async def post_update_profile(member_request_update: MemberRequestUpdate) -> MemberInfo:
    return MemberInfo(email=fake.email(), nickname=member_request_update.nickname, providerEmail=fake.email())


@router.delete("/remove", name="회원 삭제")
async def delete_member() -> Result:
    return Result(result="OK")
