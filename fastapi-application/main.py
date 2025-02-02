import uvicorn
from contextlib import asynccontextmanager
from core.db_helper import db_helper
from fastapi import FastAPI

from api import router as api_router
from core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    print("exit!!!!!!!!!!")
    await db_helper.dispose()

app = FastAPI(
    lifespan=lifespan,
    )
app.include_router(
    api_router,
    prefix=settings.api.prefix,
)


if __name__ == "__main__":
    uvicorn.run(app="main:app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True
                )
