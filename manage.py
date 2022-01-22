import os
from dotenv import load_dotenv
from app import app

app_folder = os.path.expanduser("./")
load_dotenv(os.path.join(app_folder, ".env"))

if __name__ == "__main__":
    app.run()
