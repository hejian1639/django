from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client.myproject
collection = db.myproject

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



def mongo_list(request):
    if request.method == 'GET':
        ret = []
        for doc in collection.find():
            print doc
            del doc["_id"]
            ret.append(doc)

        return HttpResponse(json.dumps(ret))


def mongo_object(request, id):
    object = collection.find_one({"id":id})
    if(object == None):
        return HttpResponse(status=404)

    del object["_id"]
    print json.dumps(object)
    if request.method == 'GET':
        return HttpResponse(json.dumps(object))

