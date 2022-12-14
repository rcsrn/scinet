from .models import Institution
from .models import GeneralUser
from .models import Journal
from .models import Publication
from .models import Topic
from import_export import resources

class InstitutionResource(resources.ModelResource):
    class Meta: 
        model = Institution
        exclude = ("id",)
        import_id_fields = ('institution_id',)
        
class JournalResource(resources.ModelResource):
    class Meta: 
        model = Journal
        import_id_fields = ('journal_id',)
        exclude = ('id')
    
class PublicationResource(resources.ModelResource):
    class Meta: 
        model = Publication
        import_id_fields = ('publication_id',)
        exclude = ('id')
        
class GeneraluserResource(resources.ModelResource):
    class Meta: 
        model = GeneralUser
        exclude = ('id')
        import_id_fields = ('general_user_id',)
        
class TopicResource(resources.ModelResource):
    class Meta:
        model = Topic
        exclude = ('id')
        import_id_fiels = ('topic_id')