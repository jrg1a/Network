from flask import Flask
from routes.config_routes import set_routes
from src.models.device_config import DeviceConfig
from src.controllers.config_controller import ConfigController
from src.services.s3_service import S3Service

def create_app():
    app = Flask(__name__)

    # Initialiser S3Service
    s3_service = S3Service(
        bucket_name='your-bucket-name',
        aws_access_key='your-access-key',
        aws_secret_key='your-secret-key'
    )

    # Initialiser ConfigController med DeviceConfig og S3Service
    device_config_model = DeviceConfig()
    config_controller = ConfigController(device_config_model, s3_service)

    # Registrer routes :D 
    set_routes(app, config_controller)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)