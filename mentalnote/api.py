from tastypie.api import *
from tastypie.resources import ModelResource
from mentalnote.models import Note

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'

#api resources from tastypie
api = Api(api_name="v1")
api.register(NoteResource())
