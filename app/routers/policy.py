from fastapi import APIRouter

from app.dependencies import fake
from app.models.policy.policy_model import PolicyModel
from app.models.result import Result

router = APIRouter(
    prefix="/api/v1/policy",
    tags=["정책"])


@router.post("", name="정책 생성")
async def post_create_policy(policy_model: PolicyModel) -> PolicyModel:
    context = ""
    for i in range(10):
        context = context + fake.text() + " "
    return PolicyModel(context=context, createdAt=fake.date(), modifiedAt=fake.date(), title=fake.sentence())


@router.put("", name="정책 수정")
async def post_update_policy(policy_model: PolicyModel) -> PolicyModel:
    context = ""
    for i in range(10):
        context = context + fake.text() + " "
    return PolicyModel(context=context, createdAt=fake.date(), modifiedAt=fake.date(), title=fake.sentence())


@router.get("/{id}", name="정책 조회")
async def get_policy(id: int) -> PolicyModel:
    context = ""
    for i in range(10):
        context = context + fake.text() + " "
    return PolicyModel(context=context, createdAt=fake.date(), modifiedAt=fake.date(), title=fake.sentence())


@router.delete("/{id}", name="정책 삭제")
async def delete_policy(id: int) -> Result:
    return Result(result="OK")

