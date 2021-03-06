# Python Imports
import uuid, datetime

# Django Imports
from django.shortcuts import render

# App Imports
from locations.models import City
from accounts.models import User
from formtools.wizard.views import SessionWizardView

# Relative Imports
from .models import ArtPiece, Hint
from .forms import ArtPieceForm


def studio(request):
    """ The studio view displays a users' drop creations. """
    if (request.user.is_anonymous()):
        return render(request, 'studio.html',{})
    artpieces = ArtPiece.objects.filter(creator=request.user)
    return render(request, 'secured-pages/studio.html',{'artpieces':artpieces})
    
def create(request):
    """ The create view is the first step in creating a drop & is used only as a preview. """
    if request.method == 'POST':
        form =ArtPieceForm(request.POST, request.FILES) 
        if form.is_valid():
            drop = form.save(commit=False)
            drop.creator = User.objects.get(username=request.user)  # use your own profile here
            drop.city = drop.creator.location
            drop.uuid = str(uuid.uuid4())   
            drop.save()
            return render(request, 'secured-pages/created.html',{'uuid':drop.uuid[:8]})
            
    else:
        form = ArtPieceForm()
        unique_drop_id = str(uuid.uuid4())
        return render(request, 'secured-pages/create.html',{'form':form,'uuid':unique_drop_id})

def drop_now(request, pk):
    artpiece = ArtPiece.objects.get(pk=pk)
    return render(request, 'secured-pages/step1.html', {"artpiece":artpiece})

def browse(request):
    drops = ArtPiece.objects.filter(city=request.user.location)
    return render(request, 'secured-pages/browse.html', {'drops_in_area':drops})        


class AWizard( SessionWizardView ):
   def get_form_initial(self, step):
    print(self.kwargs['pk'])
    return 'hi'
   def done(self, form_list, **kwargs): 

    instance = Hint()
    for form in form_list:
        for key, value in form.cleaned_data.items():
            setattr(instance, key, value)
        instance.save()
    return render(self.request, 'secured-pages/done.html', {
'form_data': [form.cleaned_data for form in form_list],
})