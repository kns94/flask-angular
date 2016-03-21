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
        return jsonify({'status': 'Error!', 'message': 'Please use POST request'})
    else:
        data = request.get_json(silent = True)
        arg1 = data['arg1']
        rel = data['rel']
        arg2 = data['arg2']

        hash_name = 'runset_map'
        hash_key = '{0}_{1}_{2}'.format(arg1, rel, arg2)

        runset_id = RedisCache.fetchValue(hash_name, hash_key, 'runset_id')

        modler = ResultModels()
        response = modler.show_result(int(runset_id))
        fetched_data = json.loads(response.text)

        result_id = modler.get_resultId(int(runset_id))
        #print fetched_data

        #print 'result_id:'+str(result_id)
        '''Changing dictionary key'''
        if len(fetched_data['data']) > 0: 
            items = fetched_data['data']
            new_data = []
            for item in items:
                new_item = {}
                filtered_item = {}
                for key, value in item.iteritems():
                    #print key, value
                    if str(key) == 'r'+str(result_id):
                        #print key
                        key = 'normalized'
                    if str(key) == 'r'+str(result_id)+'_bool':
                        #print key
                        key = 'value'
                    new_item[key] = value
                #Add a link, color
                #http://localhost:4000/runs/83/explain?claim_id=7758
                new_item['link'] = 'http://localhost:4000/runs/'+str(result_id)+'/explain?claim_id='+str(new_item['claim_id'])
                if new_item['value'] == 't':
                    new_item['color'] = 'Green'
                else:
                    new_item['color'] = 'Red'
                
                filtered_item['color'] = new_item['color']
                filtered_item['link'] = new_item['link']
                filtered_item['normalized'] = new_item['normalized']
                filtered_item['unique_key'] = new_item['property_key']+'_'+new_item['object_key']
                filtered_item['property_value'] = new_item['property_value']
                filtered_item['source_id'] = new_item['source_id']
                filtered_item['claim_id'] = new_item['claim_id']
                filtered_item['key_value'] = str(filtered_item['unique_key'])+'_'+str(new_item['property_value'])
                filtered_item['source_link'] = str(RedisCache.fetchValue('source_map', hash_key, filtered_item['source_id']))

                new_data.append(filtered_item)

            fetched_data['data'] = new_data

        """
        ''' Combining Keys'''
        if len(fetched_data['data']) > 0:
            items = fetched_data['data']
            new_data = []
            #claims = {}
            for item in items:
                unique_key = tem['property_key']+'_'+item['object_key']
                if unique_key in claims:
                    current_source = claims[unique_key]['source_id']
                    if current_source != item['source_id']:
                        new_source = current_source+','+item['source_id']
                else:
                    claims[unique_key] = {'normalized': item['normalized'], 'link': item['link'], 'color': item['color'], 'property_key': item['property_key'], 'property_value': item['property_value'], 'unique_key': unique_key, 'source_id': item['source_id']}
        """

        '''Sorting Keys'''
        if len(fetched_data['data']) > 0:
            items = fetched_data['data']
            positive = []
            negative = []
            for item in items:
                if item['color'] == 'Green':
                    positive.append(item)
                else:
                    negative.append(item)

            positive = sorted(positive, key=lambda k: k['normalized'], reverse = True) 
            negative = sorted(negative, key=lambda k: k['normalized'], reverse = True) 
            newlist = positive + negative
            fetched_data['data'] = newlist
            #print newlist
            #print '\n\n\n'

        '''Combining Sources'''
        if len(fetched_data['data']) > 0:
            extracted_data = fetched_data['data']
            combined_data = []
            for dat in extracted_data:
                value = filter(lambda item: item['key_value'] == dat['key_value'], combined_data)
                if len(value) == 0:
                    current_value = dat
                    current_value['combined_sources'] = []
                    current_value['combined_sources'].append({'id': dat['source_id'], 'link': dat['link'], 'source_link': dat['source_link']})
                    combined_data.append(current_value)
                else:
                    for item in combined_data:
                        if item['key_value'] == dat['key_value']:
                            for k,v in item.iteritems():
                                if k == 'combined_sources':
                                    item['combined_sources'].append({'id': dat['source_id'], 'link': dat['link'], 'source_link': dat['source_link']})
            fetched_data['data'] = combined_data
            #print combined_data

        if response.status_code != 200:
            return jsonify({'status': 'Error!', 'message': 'No result found'})
        else:
            return jsonify({'status': 'Success!', 'message': 'Result found', 'data': fetched_data['data']})