from usecase.user_usecase import UserUseCase
from infrastructure.user_repository_impl import InMemoryUserRepository


def test_get_user_found():
    usecase = UserUseCase(InMemoryUserRepository())
    user = usecase.get_user(1)
    assert user is not None
    assert user.id == 1


def test_get_user_not_found():
    usecase = UserUseCase(InMemoryUserRepository())
    user = usecase.get_user(999)
    assert user is None
