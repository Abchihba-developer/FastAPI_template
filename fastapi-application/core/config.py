from pydantic import BaseModel
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()
Postgresql = os.getenv("DB_URL_POSTGRESQL")

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8080

class ApiPrefix(BaseModel):
    prefix: str = "/api"

class DatabaseConfig(BaseModel): 
    db_url: str = Postgresql  # postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()

settings = Settings()
