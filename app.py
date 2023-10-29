from flask import Flask
import config  # 导入配置文件
from exts import db, mail  # 从扩展文件导入db
from models import UserModel  # 从类模型文件导入需要的模型
from blueprints.oa import bp as oa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(config)  # 绑定配置文件


db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)


app.register_blueprint(oa_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def hello_world():  # put application's code here
	return 'Hello World!'


if __name__ == '__main__':
	app.run()
