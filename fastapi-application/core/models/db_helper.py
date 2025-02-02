from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
    )
from core.config import settings


class DatabaseHelper:
    
    def __init__(self, 
                url: str, 
                echo: bool = False,
                echo_pool: bool = False,
                pool_size: int = 5,
                max_overflow: int = 10,
                ):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False, # We turn all this off because 
            autocommit=False, # we have an async engine and we will use avait!
            expire_on_commit=False,
        )

async def dispose(self): # engine completion
    await self.engine.dispose()


async def session_getter(self):
    async with self.session_factory() as session:
        yield session


db_helper = DatabaseHelper(
    url=settings.db.db_url,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)
