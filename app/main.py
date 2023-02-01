import time
from turtle import pos

import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI

from . import models
from .database import engine
from .routes import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while (True):
    try:
        # Use environment variables here
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='joshua', password='konekoya', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
