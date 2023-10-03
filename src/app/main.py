from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.db import init_db
from app.routes import router
from app.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    default_response_class=HTMLResponse,
)
app.include_router(router)
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")


@app.on_event("startup")
async def init_tables():
    await init_db()
