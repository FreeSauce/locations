from django.shortcuts import render

# Create your views here.
def studio(request):
    return render(request, 'studio.html',{})
