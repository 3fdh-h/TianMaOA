
# 数据库配置信息
import smtpd

HOSTNAME = "localhost"
PORT = "3306"
DATABASE = "tianmaoa"
USERNAME = "root"
PASSWORD = "123456"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# 邮箱配置信息
MAIL_SERVER = "smtp.163.com"
MAIl_USE_SSL = True
MAIL_TLS = False
MAIL_PORT = 465
MAIL_USERNAME = "l18972951750@163.com"
MAIL_PASSWORD = "NSEKRYRAOIMQPFVR"
MAIL_DEFAULT_SENDER = "l18972951750@163.com"
