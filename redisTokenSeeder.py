'''
Saving values into redis db
'''

from app.models import RedisCache

class RedisTokenSeed(object):
    
    def clearDB(self):
        """
        Flush database
        """
        RedisCache.clear()

    def putTokens(self):
        """
        Saving query and concerned database value
        """
        RedisCache.createHash('dataset_map','people_killed_parisAttacks', {'dataset_url': 'https://docs.google.com/spreadsheets/d/1BIUVypETaWmTCxfkvCcZlkAh4bNUP8zA94r7jPjBzbE/export?format=csv', 'dataset_id': None})
        RedisCache.createHash('runset_map','people_killed_parisAttacks', {"runset_id": None, "dataset_id": None, "checked_algo": {"Accu": ["0.2", "0", "100", "0.5", "false", "true", "true", "false"]}, "general_config": ["0.001", "0.8", "1", "0.4"]})