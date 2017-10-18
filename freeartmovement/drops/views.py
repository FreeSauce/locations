import uuid, datetime
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import ArtPiece
from locations.models import City

# Create your views here.
def studio(request):
    artpieces = ArtPiece.objects.filter(creator=request.user)
    return render(request, 'studio.html',{'artpeices':artpieces})

def create(request):
    unique_drop_id = str(uuid.uuid4())
    trimmed_drop_id = unique_drop_id[:8]
    if request.method == 'POST':
        title = request.POST['title']
        confirmed_drop_id = request.POST['uuid']

        user = User.objects.first()
        city = City.objects.first()
        drop = ArtPiece.objects.create(
        creator = user,
    	title = title,
    	city = city,
    	created_at = datetime.datetime.now(),
    	url_slug = title,
    	likes = 5
        )
        return render(request, 'created.html',{'uuid':unique_drop_id})
    return render(request, 'create.html',{'uuid':unique_drop_id})
