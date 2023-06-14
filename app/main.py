from fastapi import FastAPI
import model
from config import engine
import router
from celery_app import celery_app
from tasks import add

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def Home():
    return "Welcome Home"

@app.get("/root")
async def root():
    result = add.delay(4, 5)  # Execute the Celery task asynchronously
    return {"task_id": result.id}

app.include_router(router.router, prefix='/book', tags=['book'])
