from flask import Flask,session
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_sqlalchemy import SQLAlchemy
# 可以用来指定session保存的位置
from flask_session import Session
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand


class Config(object):
    # 项目配置
    DEBUG = True

    SECRET_KEY = "0Ny8BR09nxL+IcO7/ibQhwWTW436HkZLTwPUYLbjDj10Vj3BOsC5rMj9SCUYBHx4"

    # 为mysql添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information_flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session保存配置
    SESSION_TYPE = "redis"
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指定session保存的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化Redis存储对象
redis_store = StrictRedis(host=1234, port=Config.REDIS_PORT)
# 开启当前项目CSRF保护,只做服务器验证功能
CSRFProtect(app)
# 设置session保存指定位置
Session(app)


manager = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)



@app.route('/')
def index():
    session["name"] = "itheima"
    return 'index333'


if __name__ == '__main__':
    manager.run()