from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import FastAPI, status
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class PostSchema(BaseModel):
    some_value: str


@app.get("/")
def read_root():
    return {"status": "running", "service": "sample-service"}


@app.post("/post")
def create_user(post_schema: PostSchema):
    return JSONResponse(status_code=200, content={
        "some_value": post_schema.some_value
    })


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
