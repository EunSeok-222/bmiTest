import atexit
from flask import Flask
from config import Config
from backend.models.db import Database
from backend.routes.main_routes import main_bp, init_db


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # 1. DB 인스턴스 생성
    db = Database()
    
    # 2. Blueprint(main_routes)에 DB 객체 주입
    init_db(db)
    
    # 3. 앱 종료 시 DB 연결 해제 등록
    atexit.register(db.close)

    app.register_blueprint(main_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5002, debug=app.config['DEBUG'])