import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app=Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'backend.sqlite'),
    )
    if test_config is None:
        # load the instance of config, if it exits, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # insure the instance folder exits
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return 'Hello, World! from Osama'
    return app