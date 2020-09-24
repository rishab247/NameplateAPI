import pypyodbc
from flask import Flask, jsonify, request, make_response, logging
import jwt
import json
import datetime
from functools import wraps

app = Flask(__name__)

app.config[
    'SECRET_KEY'] = 'supsd3123xdf3232c32s32a3s'




def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.args.get('token')
        if not token:
            return jsonify({'msg': 'token req', }), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'msg': 'token is not valid', }), 401
        return f(data, *args, **kwargs)

    return decorated



@app.route('/')
def Start():
    return jsonify({'msg': 'Hello World!'}), 200


@app.route('/About')
def About():
    return jsonify({'About': 'STUFFFF'}), 200


# @app.route('/test')
# @token_required
# def test(data):
#     query = "SELECT  *  FROM [dbo].[Status] where Euid = ? + ? "
#     result = db.query(query,1 , [data['user'][:int(len(data['user'])/2)],data['user'][int(len(data['user'])/2):]])
#     print(result)
#     return jsonify({'Status': str(result)  }), 200

@app.route('/Alert')
def Alert():
    return jsonify({'msg': 'Alert!'}), 200


@app.route('/Verify', methods=['GET'])
@token_required
def Verify(data):
    query = "SELECT  [Status] ,[HOD] FROM [dbo].[Status]where Euid = ? "
    result = db.query(query, 0, [data['user']])
    return jsonify({'Status': result[0],
                    'Hod': result[1]}), 200

