import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    """Bot configuration class"""
    
    # Telegram Bot
    BOT_TOKEN: str = os.getenv('BOT_TOKEN', '')
    
    # Database
    DB_HOST: str = os.getenv('DB_HOST', 'localhost')
    DB_PORT: int = int(os.getenv('DB_PORT', '5432'))
    DB_NAME: str = os.getenv('DB_NAME', 'license_bot')
    DB_USER: str = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD', '')
    
    # Redis
    REDIS_HOST: str = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT: int = int(os.getenv('REDIS_PORT', '6379'))
    REDIS_DB: int = int(os.getenv('REDIS_DB', '0'))
    
    # FastAPI
    API_HOST: str = os.getenv('API_HOST', '0.0.0.0')
    API_PORT: int = int(os.getenv('API_PORT', '8000'))
    API_SECRET_KEY: str = os.getenv('API_SECRET_KEY', 'your-secret-key-change-me')
    
    # Crypto
    COINGATE_API_KEY: str = os.getenv('COINGATE_API_KEY', '')
    BINANCE_API_KEY: str = os.getenv('BINANCE_API_KEY', '')
    BINANCE_API_SECRET: str = os.getenv('BINANCE_API_SECRET', '')
    
    # Web3
    ETHEREUM_NODE_URL: str = os.getenv('ETHEREUM_NODE_URL', '')
    BITCOIN_NODE_URL: str = os.getenv('BITCOIN_NODE_URL', '')
    
    # Payment
    YOOMONEY_TOKEN: Optional[str] = os.getenv('YOOMONEY_TOKEN')
    STRIPE_API_KEY: Optional[str] = os.getenv('STRIPE_API_KEY')
    
    # Admin
    ADMIN_IDS: list = [int(id) for id in os.getenv('ADMIN_IDS', '').split(',') if id]
    
    # Logging
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    
    @property
    def database_url(self) -> str:
        """Returns formatted database URL"""
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def redis_url(self) -> str:
        """Returns formatted Redis URL"""
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
