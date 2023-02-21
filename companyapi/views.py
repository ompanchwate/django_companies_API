from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home page.......")
    names = [
        'hello',
        'new',
        'old'
    ]
    return JsonResponse(names, safe = False)