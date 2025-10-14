from pydantic_settings import BaseSettings, SettingsConfigDict

class JWTSettings(BaseSettings):
    algorithm: str = 'HS256'
    secret_key: str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_nested_delimiter="__")

    jwt: JWTSettings

settings = Settings()
