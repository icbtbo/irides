import collections
import functools
import json
import flask
from flask import Response
from passlib import hash
from flask_restful_swagger_2 import Api
from flask_jwt import JWTError


class MyApi(Api):
    """A simple class to keep the default flask_jwt.JWTError behaviour."""

    def __init__(self, *args, **kwargs):
        # 修改默认值,默认情况一个api对象下编写的swagger文档会挂载到某个url
        # 但是该项目创建了多个api实例,为了让swagger文档统一到一个url,取消了上述的默认行为
        if not kwargs.get('add_api_spec_resource'):
            kwargs.update({'add_api_spec_resource': False})
        super().__init__(*args, **kwargs)

    def handle_error(self, e):
        if isinstance(e, JWTError):
            return flask.jsonify(
                collections.OrderedDict([
                    ('status_code', e.status_code),
                    ('error', e.error),
                    ('description', e.description),
                ])
            ), e.status_code, e.headers
        return super(MyApi, self).handle_error(e)


def get_hash_algorithm(hash_algorithm):
    """Returns a object with methods to encrypt a string and verify a hash.

    :hash_algorithm: a string object
    :returns: hash function

    """

    available_methods = {
        'SHA256': hash.sha256_crypt,
        'SHA512': hash.sha512_crypt,
    }

    if not isinstance(hash_algorithm, str):
        raise ValueError('The parameter "hash_algorithm" should be a string.')

    if hash_algorithm.upper() not in available_methods:
        raise ValueError('Invalid hash method.')

    return available_methods[hash_algorithm]


def encrypt_password(plaintext):
    """Generate a hash based on current_app HASH_ALGORITHM.
    注意 该函数依赖了flask对象,在测试中必须在flask启动后该函数才能执行
    :plaintext: a string object.
    :returns: a string object.

    """

    method = get_hash_algorithm(flask.current_app.config['HASH_ALGORITHM'])

    return method.encrypt(
        plaintext, salt=flask.current_app.config['HASH_SALT'])


def verify_password(password, hash):
    """Verify if a hash was generated by the password specified.

    :password: a string object (plaintext).
    :hash: a string object.
    :returns: True or False.

    """

    method = get_hash_algorithm(flask.current_app.config['HASH_ALGORITHM'])

    return method.verify(password, hash)


def standardize_api_response(function):
    """ 创建标准化Api,该函数应作为装饰器使用.
    :function: 被装饰的函数应当返回dict,该字典的键中必须有一个是下面其中一个
        success -> GET, 200
        error -> Bad Request, 400
        created -> POST, 201
        updated -> PUT, 200
        deleted -> DELETE, 200
        no-data -> No Content, 204

    :returns: json.dumps(response), staus code
    """

    available_result_keys = [
        'success', 'error', 'created', 'updated', 'deleted', 'no-data']

    status_code_and_descriptions = {
        'success': (200, 'Successful Operation'),
        'error': (400, 'Bad Request'),
        'created': (201, 'Successfully created'),
        'updated': (200, 'Successfully updated'),
        'deleted': (200, 'Successfully deleted'),
        'no-data': (204, '')
    }

    @functools.wraps(function)
    def make_response(*args, **kwargs):
        result = function(*args, **kwargs)

        if not set(available_result_keys) & set(result):
            raise ValueError('Invalid result key.')

        status_code, description = status_code_and_descriptions[
            next(iter(result.keys()))
        ]

        status_code = ('status_code', status_code)
        description = (
            ('description', description) if status_code[1] != 400 else
            ('error', description)
        )
        data = (
            ('data', next(iter(result.values()))) if status_code[1] != 204 else
            ('data', '')
        )

        format = json.dumps(collections.OrderedDict([
            status_code, description, data]))
        return Response(
            response=format,
            mimetype="application/json"
        )

    return make_response


class SwgHelper:
    @staticmethod
    def Operation(tags: list = [],
                  description: str = '',
                  parameters: list = None,
                  security: list = None,
                  responses: object = None,
                  reqparser:object=None) -> object:
        d = locals()
        if not reqparser:
            d.pop('reqparser')
        else:
            d.pop('parameters')
        return d

    @staticmethod
    def Parameter(name='未填写', _in="formData",required=False , description="描述未填写", type="string", default='默认值未填写',schema=None,**kwargs):
        d=locals()
        d.pop('_in')
        d.update({'in':_in})
        d.update(kwargs)
        d.pop('kwargs')
        return d

    @staticmethod
    def Item(type='string'):
        d = dict()
        d.update(locals())
        return d

    @staticmethod
    def Response(description="描述未填写",schema=None,example=None,**kwargs):
        d = kwargs
        d.update({"description": description})
        if schema:
            d.update({"schema": schema})
        if example:
            #Reponse下有example和examples属性,两个属性不能同时使用
            d.update({"examples": {"application/json": example}})
        return d
    @staticmethod
    def SecurityRequire(name):
        d=dict()
        d.update({name:[]})
        return d