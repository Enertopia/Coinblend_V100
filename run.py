from app import create_app
from config import app_config

app = create_app(config=app_config)

if __name__ == "__main__":
    app.run()
