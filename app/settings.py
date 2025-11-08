from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "catalog-service"
    DB_HOST: str = "catalog-postgres"
    DB_PORT: int = 5432
    DB_USER: str = "catalog"
    DB_PASSWORD: str = "catalogpw"
    DB_NAME: str = "catalogdb"

    class Config:
        env_file = ".env"

settings = Settings()
