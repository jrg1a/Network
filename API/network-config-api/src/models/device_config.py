class DeviceConfig:
    def __init__(self, device_type, hostname, config_data):
        self.device_type = device_type
        self.hostname = hostname
        self.config_data = config_data

    def get_device_info(self):
        return {
            "device_type": self.device_type,
            "hostname": self.hostname,
            "config_data": self.config_data
        }