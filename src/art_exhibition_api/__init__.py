from flask import Flask

from . import db
from .config import Config
from .scheduler import scheduler

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config())

    db.init_app(app)

    scheduler.init_app(app)

    from . import tasks
    scheduler.add_job('first_task', tasks.first_task, coalesce=True, max_instances=1)
    scheduler.start()
    
    from .exhibitions import bp
    app.register_blueprint(bp)

    return app
