# Import
from django.http import HttpResponse, JsonResponse

# View
def hello(request):
    print("Bonjour")
    return HttpResponse("Hello World!")
    # return JsonResponse(
    #     {
    #         'message':'Hello',
    #         'price': 15.45,
    #         'available': True,
    #     }
    #     )

