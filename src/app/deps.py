from typing import AsyncGenerator

from app.db import async_session


async def async_get_db() -> AsyncGenerator:
    async with async_session() as session:
        yield session
