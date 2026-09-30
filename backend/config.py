import os
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

ENV_PATH = os.path.join(
    BASE_DIR,
    ".env"
)

load_dotenv(ENV_PATH)


MODEL_TYPE = "gemini"

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


print("Gemini key loaded:", GEMINI_API_KEY is not None)
print("ENV PATH:", ENV_PATH)
print("KEY EXISTS:", GEMINI_API_KEY is not None)