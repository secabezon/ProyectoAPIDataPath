from fastapi import FastAPI, HTTPException, status
from routes import router

app=FastAPI()
app.include_router(router)