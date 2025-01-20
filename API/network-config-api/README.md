# Network Config API

Tired of always looking up and typing the same configuration commands? This API service is for retrieving and managing configurations for network devices such as routers and switches, specifically Cisco devices, that you can use when labbing or testing network configurations.

## Project Structure

```
network-config-api
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── controllers
│   │   ├── __init__.py
│   │   └── config_controller.py
│   ├── models
│   │   ├── __init__.py
│   │   └── device_config.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── config_routes.py
│   └── services
│       ├── __init__.py
│       └── s3_service.py

├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd network-config-api
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```
   python src/app.py
   ```
2. Access the API endpoints to retrieve and manage device configurations.

## API Endpoints

- `GET /api/configurations`: Retrieve all device configurations.
- `POST /api/configurations`: Store a new device configuration.
- `GET /api/configurations/<device_id>`: Retrieve a specific device configuration.
- `PUT /api/configurations/<device_id>`: Update a specific device configuration.
- `DELETE /api/configurations/<device_id>`: Delete a specific device configuration.


## Inspiration
I got tired of writing the same base configurations for my lab switch and router devices, so I decided to try create an API that would store and retrieve these configurations for me. This project is a work in progress and I plan to add more features and functionality to it, after practicing and learning more about APIs and Python - and last but not least, testing it out in my lab environment.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.