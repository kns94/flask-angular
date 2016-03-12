from flask import render_template, request, redirect, Blueprint, session, jsonify
import requests, json

#Models 
from app.models import RedisCache
from app.models import ResultModels
import json, ast, pickle

result = Blueprint("result", __name__, url_prefix="/result")

@result.route("/show", methods = ['GET', 'POST'])
def show_result():
    """
    Show runset result
    """
    if request.method == 'GET':
        arg1 = request.args.get('arg1')
        arg2 = request.args.get('arg2')
        rel = request.args.get('rel')

        hash_name = 'runset_map'
        hash_key = '{0}_{1}_{2}'.format(arg1, rel, arg2)
        runset_id = RedisCache.fetchValue(hash_name, hash_key, 'runset_id')

        
        return jsonify({'status': 'Error!', 'message': 'Please use POST request'})
    else:
        data = request.get_json(silent = True)
        arg1 = data['arg1']
        rel = data['rel']
        arg2 = data['arg2']

        hash_name = 'runset_map'
        hash_key = '{0}_{1}_{2}'.format(arg1, rel, arg2)

        runset_id = RedisCache.fetchValue(hash_name, hash_key, 'runset_id')
        #print runset_id

        modler = ResultModels()
        response = modler.show_result(int(runset_id))
        #print response.text
        data = json.loads(response.text)

        if response.status_code != 200:
            return jsonify({'status': 'Error!', 'message': 'No result found'})
        else:
            return jsonify({'status': 'Success!', 'message': 'Result found', 'data': data})