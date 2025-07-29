from domain.user_repository import UserRepository
from domain.user_entity import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {
            1: User(id=1, name="Alice", email="alice@example.com"),
            2: User(id=2, name="Bob", email="bob@example.com"),
        }

    def get_user_by_id(self, user_id: int):
        return self.users.get(user_id)
