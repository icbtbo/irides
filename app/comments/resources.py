from flask_restful import Resource, reqparse
from flask_jwt import jwt_required,current_user
from flask_restful_swagger_2 import swagger, Schema
from flask import current_app, request
from app import helpers, extensions, UserLoginSchema
from app.helpers import SwgHelper
from . import controllers

class CommentAPI(Resource):
    """
    获取或添加评论
    """
    parse_post = reqparse.RequestParser()
    parse_post.add_argument(
        'userId', type=int, location='json', required=True)
    parse_post.add_argument(
        'picId', type=int, location='json', required=True)
    parse_post.add_argument(
        'content', type=str, location='json', required=True)
    parse_post.add_argument(
        'time', type=str, location='json', required=True)
    parse_post.add_argument(
        'reply_to', type=int, location='json', required=True)

    parse_get = reqparse.RequestParser()
    parse_get.add_argument(
        'picId',type=int, location='args', required=True
    )
    # 添加评论
    @jwt_required()
    @helpers.standardize_api_response
    def post(self):
        args = self.parse_post.parse_args()
        userId, picId, content, time, reply_to = args['userId'], args['picId'], args['content'], args['time'], args['reply_to']
        return controllers.post_comments(userId,picId,content,time,reply_to)

    # 获取评论以及最后一条评论的id
    def get(self):
        args = self.parse_get.parse_args()
        picId = args['picId']
        
        return controllers.get_comments(picId)
