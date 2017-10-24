import uuid, datetime
from django.shortcuts import render

from .models import ArtPiece
from locations.models import City
from accounts.models import User

# Create your views here.
def studio(request):
    if (request.user.is_anonymous()):
        return render(request, 'studio.html',{})
    artpieces = ArtPiece.objects.filter(creator=request.user)
    print (artpieces)
    return render(request, 'secured/studio.html',{'artpieces':artpieces})
    

def create(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        confirmed_drop_id = request.POST['uuid']

        user = User.objects.first()
        city = City.objects.first()
        drop = ArtPiece.objects.create(
        creator = user,
    	title = title,
    	city = city,
        uuid = confirmed_drop_id,
        trimmed_uuid = confirmed_drop_id[:8],
    	created_at = datetime.datetime.now(),
    	url_slug = title,
    	likes = 5
        )
        return render(request, 'secured/created.html',{'uuid':confirmed_drop_id[:8]})
    unique_drop_id = str(uuid.uuid4())
    return render(request, 'secured/create.html',{'uuid':unique_drop_id})
