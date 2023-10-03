from fastapi import APIRouter, Depends, Request
from jinja2_fragments.fastapi import Jinja2Blocks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app import deps
from app.models import User
from app.settings import settings

templates = Jinja2Blocks(directory=settings.TEMPLATE_DIR)
router = APIRouter()


@router.get("/")
async def index(
    request: Request,
    db: AsyncSession = Depends(deps.async_get_db),
):
    q = await db.execute(select(User).order_by(User.id))
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "title": "Manage users",
            "users": q.scalars().all(),
        },
    )
