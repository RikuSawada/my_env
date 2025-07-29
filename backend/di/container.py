from infrastructure.user_repository_impl import InMemoryUserRepository
from usecase.user_usecase import UserUseCase

def get_user_usecase() -> UserUseCase:
    user_repo = InMemoryUserRepository()
    return UserUseCase(user_repo)
