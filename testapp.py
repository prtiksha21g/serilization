import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.json())
#
# get_resource(1)
def create_resource():
    data={

    'name':'Darlo',
    'rollno':5,
    'city':'Banglore'

}
    res=requests.post(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(res.json())
create_resource()
# def update_resource(id):
#     new_data={
#         'id':id,
#         'city':'nanded'
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
#     print(resp.json())
# update_resource(3)
# def del_resource(id):
#     data={
#         'id':id,
#
#     }
#     r=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(r.json())
# del_resource(3)