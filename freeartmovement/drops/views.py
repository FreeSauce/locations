import uuid
from django.shortcuts import render

# Create your views here.
def studio(request):
    return render(request, 'studio.html',{})

def create(request):
    unique_drop_id = str(uuid.uuid4())
    trimmed_drop_id = unique_drop_id[:8]
    return render(request, 'create.html',{'trimmed_uuid':trimmed_drop_id})
