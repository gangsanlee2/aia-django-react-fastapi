import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

from basic.dlearn.fashion.services import FashionService

@api_view(['GET', 'POST'])
def fashion(request):
    if request.method == 'GET':
        print(f"######## ID is {request.GET['id']} ########")
        return JsonResponse(
            {'result': FashionService().service_model(int(request.GET['id']))})
    elif request.method == 'POST':
        data = json.loads(request.body)  # json to dict, 엄밀하게 말하면 key 없이 value만 넘어옴
        print(f"######## {data} type is {type(data)} ########")
        result = FashionService().service_model(int(data))
        print(f"######## result is {result} ########")
        return JsonResponse({'result': result})
    else:
        print(f"##### ID is None #####")
