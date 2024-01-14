from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("""
    #<html>
    #<head>
    #<title>Account Ripper</title>
    #</head>
    #<body>
    #<h1>Account Ripper</h1>
    #<p>Account Ripper is a tool that allows you to rip accounts from various websites.</p>
    #<p>It is currently in development.</p>
    #</body>
    #</html>
    #""")
    #return index.html in the templates
    if request.htmx:
        print("This is an htmx request")
        print(request.htmx)
    return render(request, "home.html")

def index(request):
    if request.htmx:
        print("This is an htmx request")
        print(request.htmx)
        return render(request, "text.html")
    return render(request, "index.html")

def test(request):
    if request.htmx:
        print("This is an htmx request")
        print(request.htmx)
    return render(request, "test.html")