from .models import Institution
from .models import GeneralUser
from .models import Journal
from .models import Publication
from .models import Writes
from .models import Belongs
from .models import Quotes
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
        import_id_fields = ('general_user_id')
        exclude = ('id')
        
class BelongsResource(resources.ModelResource):
    class Meta: 
        model = Belongs
        exclude = ('id')
        
class QuotesResource(resources.ModelResource):
    class Meta: 
        model = Quotes
        import_id_fields = ('publication_id', )
        exclude = ('id')
        
class WritesResource(resources.ModelResource):
    class Meta: 
        model = Writes
        exclude = ('id')
        
