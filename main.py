
from fastapi import FastAPI
from routes.users.index import router as user_router
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router,prefix="/api")
