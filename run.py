from app import create_app 
from config import app_active, app_config

config = app_config[app_active]
app = create_app(app_active)


if __name__ == "__main__":
    app.run(host=config.IP_HOST, port=config.PORT_HOST, debug=True)
