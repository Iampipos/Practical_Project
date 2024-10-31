import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TAT_API_KEY = os.getenv("TAT_API_KEY")
