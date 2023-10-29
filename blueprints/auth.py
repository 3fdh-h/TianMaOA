import random
import string

from flask import Blueprint, render_template, request
from exts import mail
from flask_mail import Message


# /auth
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login')
def auth():
	pass


@bp.route('/register')
def register():
	return render_template('register.html')


@bp.route('/captcha/email')
def get_email_captcha():
	email = request.args.get("email")
	source = string.digits*4
	captcha = random.sample(source, 4)
	"".join(captcha)
	print(captcha)
	return "success"


@bp.route('/mail/test')
def mail_test():
	message = Message(subject='邮箱测试', recipients=["3175794509@qq.com"], body='这是一条测试邮件')
	mail.send(message)
	return "邮件发送成功"
