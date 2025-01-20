from flask import Blueprint, jsonify, request

def set_routes(app, config_controller):
    config_routes = Blueprint('config_routes', __name__)

    @config_routes.route('/api/configurations', methods=['GET'])
    def get_configurations():
        device_id = request.args.get('device_id')
        config = config_controller.get_device_config(device_id)
        return jsonify(config), 200

    @config_routes.route('/api/configurations', methods=['POST'])
    def store_configuration():
        data = request.json
        device_id = data['device_id']
        config_data = data['config_data']
        result = config_controller.store_device_config(device_id, config_data)
        return jsonify(result), 201

    app.register_blueprint(config_routes)