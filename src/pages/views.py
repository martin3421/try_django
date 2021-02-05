from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 312, 5432, 'ABC', 9588]
    }
    return render(request, 'about.html', context=my_context)
