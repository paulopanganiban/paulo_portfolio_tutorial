from django.shortcuts import render

# Create your views here.
def hello_word(request):
    return render(request, 'hello_world/hello_world.html', {})