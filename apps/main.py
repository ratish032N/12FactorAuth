from fastapi import FastAPI, APIRouter
import uvicorn
from apps.app import router

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello World"}

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run('server.app:app', host="0.0.0.0", port=8000, reload=True)