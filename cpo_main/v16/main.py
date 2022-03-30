from fastapi import FastAPI
from CPO import models
from CPO.database import engine
from CPO.router import user, authentication
from CPO.router import charge_point_routes
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Drifter World API")

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(charge_point_routes.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)