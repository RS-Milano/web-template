# Standard libraties
from uuid import UUID
# Moduls
from schemas import User


class UsersService:

    @staticmethod
    def get_user_by_id(id: UUID) -> User:
        return User()

users_service = UsersService()
