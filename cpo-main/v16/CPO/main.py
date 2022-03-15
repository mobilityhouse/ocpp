from fastapi import Depends, FastAPI
from . import models
from .database import engine
from .router import user, authentication, charge_point_routes


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(charge_point_routes.router)