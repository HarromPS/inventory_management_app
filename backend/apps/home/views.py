from django.http import HttpResponse

# Create your endpoints here.

# default home page 
def homePage(request):
    return HttpResponse("Welcome to backend")