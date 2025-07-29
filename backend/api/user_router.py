from fastapi import APIRouter, Depends, HTTPException
from di.container import get_user_usecase
from usecase.user_usecase import UserUseCase
from domain.user_entity import User

router = APIRouter()

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, usecase: UserUseCase = Depends(get_user_usecase)):
    user = usecase.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
