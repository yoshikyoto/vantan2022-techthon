from django.views import View
# JsonResponse を import
from django.http import JsonResponse

class CheckView(View):
    def get(self, request):
        python_dict = {
            "status_code": 200,
            "method": "GET",
        }
        return JsonResponse(python_dict)

    def post(self, request):
        python_dict = {
            "status_code": 200,
            "method": "POST",
        }
        return JsonResponse(python_dict)
