import pymongo

connection = pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])

class User:
    db = connection.users
    


