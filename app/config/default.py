# -*- coding: utf-8 -*-
import os,datetime
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
class Config:
    """
    配置基类
    """
    #密钥配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you cannot guess me'

    #数据库配置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #当连接断开时是否提交事务
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    '''
    如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
    这需要额外的内存,如果不必要的可以禁用它
    '''
    #PASSLIB
    HASH_ALGORITHM = 'SHA256'
    HASH_SALT = 'QxLUF1bgIAdeQX'
    #邮件配置
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True

    #JWT
    JWT_AUTH_URL_RULE='/api/auth'
    JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=3600)

    # 为了安全,不要把隐私信息直接写到这里会被git记录
    # 可以放到production.py,并用gitignore忽略该文件,或者就像下面这样放到系统环境变量
    # 注意pycharm可直接配置运行时环境变量,这样无需真的修改操作系统的环境变量
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = os.environ.get('MAIL_USERNAME')
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    # 七牛云配置
    QINIU_ACCESS_KEY = 'c5QClH08302zJVBGKw8KCHJ0MZ2wqnIJgRsLHNhA'
    QINIU_SECRET_KEY = '59sRtJWdiOE727BMMpnZXN2uroHsHMD6t7UcB37n'
    QINIU_BUCKET_NAME = 'iridespics'
    QINIU_DOMAIN = 'http://p7fayt0os.bkt.clouddn.com/'
    # UPLOAD_FOLDER = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\' + 'uploads'
    # MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

    @staticmethod
    def init_app(app):
        pass