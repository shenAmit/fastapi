# main.py

from fastapi import FastAPI
from views.users.index import router as user_router
import models
from database import engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register the user API router
app.include_router(user_router)
