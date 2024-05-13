import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    organization=os.getenv("ORGANIZATION"),
    project=os.getenv("PROJECT_ID"),
)
