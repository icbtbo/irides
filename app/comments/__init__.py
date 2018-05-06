from flask import Blueprint
from app import helpers
from . import resources


blueprint = Blueprint('comments', __name__)
api = helpers.MyApi(blueprint, prefix='/api')

api.add_resource(resources.CommentAPI, '/comment')
