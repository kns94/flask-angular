from flask import render_template, request, redirect, Blueprint, session, jsonify, url_for
import requests

#Models 
from app.models import RedisCache

query = Blueprint("query", __name__, url_prefix="/query")

@query.route("", methods = ['GET', 'POST'])
def parse_query():
    """
    Fetch database_id of a given query
    """

    if request.method != 'POST':
        return jsonify({'status': 'Error!', 'message': 'Please use POST request'})
    else:    
        print 'here'
        print request 
        data = request.get_json()
        #arg1 = request.form['arg1']
        #print arg1
        print data
        #print len(data) 

        if data == None:
            return jsonify({'status': 'Error!', 'message': 'Please pass parameters'})
        else:
            arg1 = data['arg1']
            rel = data['rel']
            arg2 = data['arg2']

            hash_name = 'dataset_map'
            hash_key = '{0}_{1}_{2}'.format(arg1, rel, arg2)
        
            if not RedisCache.isExists(hash_name, hash_key):
                return jsonify({'status': 'Error!', 'message': 'Key does not exists'})
            else:
                value = RedisCache.fetchValue(hash_name, hash_key, 'dataset_id')

                if value == 'None':
                    return redirect(url_for('dataset.upload'), code=307)
                else:
                    return redirect(url_for('runset.create_runset'), code=307)