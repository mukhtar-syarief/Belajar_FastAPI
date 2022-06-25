from fastapi import FastAPI
# from src.models.user import User

from src.api.home_api import home
from src.api.login_api import login
from src.api.signup_api import signup
from src.api.user_api import user
from src.api.product_api import product
# from fastapi_login import LoginManager

def create_app():
    app = FastAPI()

    app.include_router(home)
    app.include_router(login)
    app.include_router(signup)
    app.include_router(user)
    app.include_router(product)

    # SECRET = "MencintaiDalamSepi"
    # login_manager = LoginManager(SECRET, "/login")

    # @login_manager.user_loader
    # def load_user(id: int):
    #     return s.query(User).filter(User.id == id).first()

    return app

app = create_app()
