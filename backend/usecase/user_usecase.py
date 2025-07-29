from domain.user_repository import UserRepository
from domain.user_entity import User
from typing import Optional

class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_user_by_id(user_id)
