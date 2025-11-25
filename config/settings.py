# config/settings.py
import os

class Settings:
    def __init__(self):
        self.model_path = os.getenv("MODEL_PATH", "./models/")
        self.debug = os.getenv("DEBUG", "False") == "True"

settings = Settings()