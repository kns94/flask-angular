'''
Models pertaining to a runset result
'''

import requests, json


class ResultModels:

    def __init__(self):
        self.user_token = 'fHRCD4f1ZLFsUN4DAqmm'
   
    def show_result(self, runset_id):
        url = "http://localhost:4000/runsets/"+str(runset_id)+"/results"
        data = {"user_token": self.user_token}
        data = json.dumps(data)
        #print data
        r = requests.get(url, data = data, headers = {'Content-Type': 'application/json'})
        return r

if __name__ == '__main__':
    modler = ResultModels()
    response = modler.show_result(39)   
    #print response
    #print response.text
    #ids = modler.fetch_ids()
    #print ids
    #modler.clear(ids)