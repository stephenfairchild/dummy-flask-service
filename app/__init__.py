from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/dummy')
    def hello():
        return 'Hello, World'

    return app
