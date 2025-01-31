import os
import json
from dotenv import load_dotenv

api_key = os.getenv('api_key')
print(f"Api key is: {api_key}")