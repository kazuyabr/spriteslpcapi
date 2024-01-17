import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT"))

if __name__ == "__main__":
    uvicorn.run("src.server:app", host="0.0.0.0", port=PORT, reload=True, reload_dirs="src")
