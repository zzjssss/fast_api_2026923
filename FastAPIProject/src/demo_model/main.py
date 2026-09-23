from contextlib import asynccontextmanager

from fastapi import FastAPI
from src.demo_model.routerss import router as routerss_router
import uvicorn

#加入生命周期
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行：加载数据库、模型等
    print("应用启动...")
    yield
    # 关闭时执行：清理资源
    print("应用关闭...")


app = FastAPI(title="My Demo API",
    description="这是一个演示项目" ,lifespan= lifespan)
app.include_router(routerss_router, prefix="/api", tags=["API"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}





if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)

