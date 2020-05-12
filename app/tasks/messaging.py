from ..application import db
from ..models.orm.user import User as ORMUser
from ..models.pydantic.user import User


async def send_message(ctx: dict, user_id: int, message: str):
    # TODO: Add a messaging service.
    orm_user: ORMUser = await ORMUser.get(user_id)
    user: User = User.from_orm(orm_user)
    print(
        "Message sent to {phone_number}: {message}".format(
            phone_number=user.phone_number, message=message
        )
    )
    return user
