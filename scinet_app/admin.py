from django.contrib import admin
from .models import Institution
from .models import Generaluser
from .models import Journal
from .models import Publication
from .models import Writes
from .models import Belongs
from .models import Quotes
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class InstitutionResource(resources.ModelResource):
    class Meta: 
        model = Institution
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id')
        exclude = ('id')
        fields = ('id', 'institution_id', 'name')
        
class InstitutionAdmin(ImportExportModelAdmin):
    resource_class = InstitutionResource
    
class GeneraluserResource(resources.ModelResource):
    class Meta: 
        model = Generaluser
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id')
        exclude = ('id')
        fields = ('id', 'general_user_id', 'username','first_name',
                  'last_name','email','age','is_alive','is_author')
        
class GenerlaluserAdmin(ImportExportModelAdmin):
    resource_class = GeneraluserResource
    
class BelongsResource(resources.ModelResource):
    class Meta: 
        model = Belongs
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id')
        exclude = ('id')
        fields = ('id', 'institution_id', 'general_useer_id')
        
class BelongsAdmin(ImportExportModelAdmin):
    resource_class = BelongsResource
    
class JournalResource(resources.ModelResource):
    class Meta: 
        model = Journal
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id')
        exclude = ('id')
        fields = ('id', 'journal_id', 'name')
        
class JournalAdmin(ImportExportModelAdmin):
    resource_class = JournalResource
    
class PublicationResource(resources.ModelResource):
    class Meta: 
        model = Publication
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id')
        exclude = ('id')
        fields = ('id', 'publication_id', 'journal_id', 'title',
                  'publication_date')
        
class PublicationAdmin(ImportExportModelAdmin):
    resource_class = PublicationResource
    
class QuotesResource(resources.ModelResource):
    class Meta: 
        model = Quotes
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id')
        exclude = ('id')
        fields = ('id', 'publication_id', 'publication_id')
        
class QuotesAdmin(ImportExportModelAdmin):
    resource_class = QuotesResource
    
class WritesResource(resources.ModelResource):
    class Meta: 
        model = Writes
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('id')
        exclude = ('id')
        fields = ('id', 'general_user_id', 'publication_id')
        
class WritesAdmin(ImportExportModelAdmin):
    resource_class = WritesResource

admin.site.register(Institution,InstitutionAdmin)
admin.site.register(Generaluser)
admin.site.register(Journal)
admin.site.register(Publication)
admin.site.register(Writes)
admin.site.register(Belongs)
admin.site.register(Quotes)
