import pickle

import requests
from flask import Flask, request, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    import config
    app.config.from_object(config)

    response = requests.get(app.config['MODEL_URL'])

    if response.status_code == 200:
        model = pickle.loads(response.content)
        print('Model loaded successfully.')
    else:
        print('Failed to download the model. Status code:', response.status_code)

    @app.route('/')
    def index():
        return jsonify({'status': 200}), 200

    @app.route('/healthcheck')
    def healthcheck():
        return jsonify({'status': 200}), 200

    def process_nested_dict(input_dict: dict) -> dict:
        updated_dict = {}

        for key, value in input_dict.items():
            if isinstance(value, dict):
                updated_dict[key] = process_nested_dict(value)
            else:
                updated_dict[key] = model.encode(value).tolist()

        return updated_dict

    @app.route('/process', methods=['POST'])
    def process():
        try:
            request_data = request.get_json()

            if not request_data or 'data' not in request_data or not isinstance(request_data['data'], dict):
                return jsonify({'status': 400, 'message': 'Invalid JSON format or data type'}), 400

            return jsonify({'status': 200, 'data': process_nested_dict(request_data['data'])}), 200

        except Exception as e:
            return jsonify({'status': 500, 'message': f'An error occurred: {str(e)}'}), 500

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7020)
