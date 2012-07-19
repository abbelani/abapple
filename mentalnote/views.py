# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from mentalnote.models import Note

def index(request):
    list_of_notes = Notes.object.all().order-by('-postedOn')
    return render_to_response('mentalnote/index.html', {'list_of_notes': list_of_notes})

def detail(request, note_id):
    n = get_object_or_404(Note, pk=note_id)
    return render_to_response('mentalnote/detail.html', {'note': n})
