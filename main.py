import importlib
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

if __name__ == "__main__":
    host = os.environ.get("HOST", "api")
    port = int(os.environ.get("PORT", 8080))
    app_api = importlib.import_module("api")
    app_api.run(host=host, port=port)
