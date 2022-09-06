from django.shortcuts import render

# Create your views here.
def dinner(request, people, menu):
    context = {
        'people' : people,
        'menu' : menu,
        }
    return render(request, 'dinner.html', context)