import uuid, datetime
from django.shortcuts import render

from .models import ArtPiece
from locations.models import City
from accounts.models import User

from .forms import ArtPieceForm

# Create your views here.
def studio(request):
    if (request.user.is_anonymous()):
        return render(request, 'studio.html',{})
    artpieces = ArtPiece.objects.filter(creator=request.user)
    print (artpieces)
    return render(request, 'secured/studio.html',{'artpieces':artpieces})
    

def create(request):
    
     if request.method == 'POST':
        form =ArtPieceForm(request.POST, request.FILES) 
        if form.is_valid():
            drop = form.save(commit=False)
            drop.creator = User.objects.get(username=request.user)  # use your own profile here
            drop.city = drop.creator.location
            drop.uuid = uuid.uuid4()
            drop.trimmed_uuid = uuid.uuid4()
            drop.save()
            return render(request, 'secured-pages/created.html',{'uuid':unique_drop_id})
            
     else:
        form = ArtPieceForm()
        unique_drop_id = str(uuid.uuid4())
        return render(request, 'secured-pages/create.html',{'form':form,'uuid':unique_drop_id})