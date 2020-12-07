import pymongo
import os 

class audio_db:
    def __init__(self):
        password=os.environ.get('mongodbPassword')
        user=os.environ.get('mongodbUser')
        connectionstring="mongodb+srv://%s:%s@clusteraudio.sq27z.mongodb.net/?retryWrites=true&w=majority"%(user,password)
        client = pymongo.MongoClient(connectionstring)
        self.db = client.AudioData

        
    def insert(self,object):
        document=self.db.results
        return document.insert_one(object)