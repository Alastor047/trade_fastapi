from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from user_auth.auth import auth_backend
from user_auth.schemas import UserRead, UserCreate
from user_auth.database import User
from user_auth.manager import get_user_manager

app = FastAPI(
    title="Trading app"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
