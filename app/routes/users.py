from fastapi import APIRouter

from ..models.orm.user import ORMUser
from ..models.pydantic.user import User, UserCreateIn, UserUpdateIn

router = APIRouter()


@router.post("/users", tags=["Users"], response_model=User)
async def create_user(request: UserCreateIn):
    new_user: ORMUser = await ORMUser.create(**request.dict())
    return User.from_orm(new_user)


@router.get("/users/{id}", tags=["Users"], response_model=User)
async def retrieve_user(id: int):
    user: ORMUser = await ORMUser.get(id)
    return User.from_orm(user)


@router.put("/users/{id}", tags=["Users"], response_model=User)
async def update_user(request: UserUpdateIn, id: int):
    user: ORMUser = await ORMUser.get(id)
    updated_fields: User = User.from_orm(request)
    await user.update(**updated_fields.dict(skip_defaults=True)).apply()
    return User.from_orm(user)


@router.delete("/users/{id}", tags=["Users"], response_model=User)
async def delete_user(id: int):
    user: ORMUser = await ORMUser.get(id)
    return await user.delete()
