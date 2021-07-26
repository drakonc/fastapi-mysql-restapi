from fastapi import FastAPI
from Routes.user import user

app = FastAPI()

@app.get('/')
def helloworld():
    return {"message":"Hello World"}

app.include_router(user)
