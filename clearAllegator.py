'''
Clear Allegator Track
'''

from app.models import DatasetModels
from app.models import RunsetModels

modeler = DatasetModels()
ids = modeler.fetch_ids('claims')
modeler.clear(ids)

modeler = RunsetModels()
ids = modeler.fetch_ids()
modeler.clear(ids)

print 'Removed Content from Allegator Track'