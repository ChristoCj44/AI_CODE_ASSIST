from pydantic import BaseModel


class Settings(BaseModel):
    APP_NAME: str = "AI Code Assist"
    VERSION: str = "1.0.0"


settings = Settings()