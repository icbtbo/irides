import os
import werkzeug,datetime
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import request, current_app, g
from werkzeug import secure_filename
from app import helpers, extensions
from . import controllers
from ..models import  Picture
from ..extensions import db


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def post_put_parser():
    """Request parser for HTTP POST or PUT.
    :returns: flask_restful.reqparse.RequestParser object
    """
    parse = reqparse.RequestParser()
    parse.add_argument(
        'file', type=werkzeug.datastructures.FileStorage, location='files', required=True)
    return parse

class PicturesAPI(Resource):
    '''
    def _post_put_parser(self):
        """Request parser for HTTP POST or PUT.
        :returns: flask_restful.reqparse.RequestParser object

        """
        parse = reqparse.RequestParser()
        parse.add_argument(
            'username', type=str, location='json', required=True)
        parse.add_argument(
            'password', type=str, location='json', required=True)

        return parse
    '''

    # @jwt_required()
    @helpers.standardize_api_response
    def get(self):
        """HTTP GET. Get all pictures"""
        num = request.args.get('number')

        return controllers.get_pictures(num)




class PictureAPI(Resource):

    # @jwt_required()
    @helpers.standardize_api_response
    def get(self):
        """HTTP GET, Get specific pictures"""
        pic_tag = request.args.get('SearchKey')
        return controllers.get_specific_picture(pic_tag)


class UploadPicAPI(Resource):

    def get(self):
        pass
    @jwt_required()
    @helpers.standardize_api_response
    def post(self):
        """HTTP Post, Upload picture"""
        parse = post_put_parser()
        args = parse.parse_args()        
        file = args['file']     
        filestream = file.read()
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            url = controllers.qiniu_upload_file(filestream, filename)
            if url != None:
                db.session.add(Picture(
                    address=url
                    # userId=g.user.id
                ))
        return {'success': 'You have uploaded a picture!'}


