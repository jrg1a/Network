from src.services.s3_service import S3Service

class ConfigController:
    def __init__(self, device_config_model, s3_service):
        self.device_config_model = device_config_model
        self.s3_service = s3_service

    def store_device_config(self, device_id, config_data):
        # Lagre konfigurasjon til S3
        file_name = f"{device_id}.txt"
        with open(file_name, 'w') as file:
            file.write(config_data)
        self.s3_service.upload_file(file_name)
        return {"message": "Configuration stored successfully."}

    def get_device_config(self, device_id):
        # Hent konfigurasjon fra S3
        file_name = f"{device_id}.txt"
        self.s3_service.download_file(file_name, file_name)
        with open(file_name, 'r') as file:
            config_data = file.read()
        return config_data
    
    