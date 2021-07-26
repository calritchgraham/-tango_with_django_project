from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    
    # return HttpResponse("Rango says hey there partner! \
    #     <br/> <a href='/rango/about/'>about</a>")
    

def about(request):
    return HttpResponse("Rango says here is the about page. \
        <br/> <a href='/rango/'>index</a>")