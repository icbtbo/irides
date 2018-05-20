from flask import current_app
from qiniu import Auth, put_stream, put_data
from app import helpers
from app import models
from app.extensions import db


def get_pictures(num):
    """Get all pictures"""
    # pictures = models.Picture.query.filter_by().all()
    pictures = models.Picture.query.order_by(models.Picture.id.desc()).limit(50).offset(int(num))    
    if not pictures:
        return {'no-data': ''}
    return {'success': [p.to_json() for p in pictures]}


def get_specific_picture(pic_tag):
    """Get specific pictures"""

    pictures = models.Picture.query.filter(models.Picture.tags.any(tag=pic_tag)).all()
    if not pictures:
        return {'no-data': ''}

    return {'success': [picture.to_json() for picture in pictures]}

def qiniu_upload_file(source_file, save_file):
    access_key = current_app.config['QINIU_ACCESS_KEY']
    secret_key = current_app.config['QINIU_SECRET_KEY']
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = current_app.config['QINIU_BUCKET_NAME']
    domain_prefix = current_app.config['QINIU_DOMAIN']
    policy = {
        "fsizeLimit": 1024*1024
    }
    token = q.upload_token(bucket_name, key=save_file, policy=policy)
    ret, info = put_data(token, save_file, source_file)
    if info.status_code == 200:
        return domain_prefix + save_file
    return None