from abc import ABC, abstractmethod
from .user_entity import User
from typing import Optional

class UserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        pass
