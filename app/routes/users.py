from fastapi import APIRouter

from ..models.orm.user import User
from ..models.pydantic.user import User as UserSchema, UserCreateIn, UserUpdateIn

router = APIRouter()


@router.post('/users', tags=['Users'], response_model=UserSchema)
async def create_user(request: UserCreateIn):
    new_user: User = await User.create(**request.dict())
    return UserSchema.from_orm(new_user)


@router.get('/users/{id}', tags=['Users'], response_model=UserSchema)
async def retrieve_user(id: int):
    user: User = await User.get(id)
    return UserSchema.from_orm(user)


@router.put('/users/{id}', tags=['Users'], response_model=UserSchema)
async def update_user(request: UserUpdateIn, id: int):
    user: User = await User.get(id)
    updated_fields: UserSchema = UserSchema.from_orm(request)
    await user.update(**updated_fields.dict(skip_defaults=True)).apply()
    return UserSchema.from_orm(user)


@router.delete('/users/{id}', tags=['Users'], response_model=UserSchema)
async def delete_user(id: int):
    user: User = await User.get(id)
    return await user.delete()
