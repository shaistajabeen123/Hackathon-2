import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

from src.main import app
import uvicorn

if __name__ == "__main__":
    # Run the server with logging enabled
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")