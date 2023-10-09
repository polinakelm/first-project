from django.http import HttpResponse

def hello_page(request):
    print(HttpResponse("<h1>Hello, World!</h1>"))
    return HttpResponse("<h1>Hello, World!</h1>")