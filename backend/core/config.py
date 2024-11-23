from pydantic import BaseSettings


class Settings(BaseSettings):
    
    DATABASE_URL: str

    CLIENT_ORIGIN: str
    COOKIES_DOMAIN: str = ""
    FRONTEND_URL: str

    API_V1_STR: str
    FIRST_SUPERUSER_EMAIL: str
    FIRST_SUPERUSER_FISCALCODE: str
    USERS_OPEN_REGISTRATION: str

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int
    EMAILS_ENABLED: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str
    JWT_PRIVATE_KEY: str
    JWT_PUBLIC_KEY: str

    

    class Config:
        env_file = '/backend/.env'


settings = Settings()
