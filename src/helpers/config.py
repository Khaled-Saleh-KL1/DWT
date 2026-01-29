from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    HF_TOKEN: str

    class Config(SettingsConfigDict):
        env_file = '.env'
    
def get_settings() -> Settings:
    return Settings()
