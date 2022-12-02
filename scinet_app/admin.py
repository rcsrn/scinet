from django.contrib import admin

from .models import Institution
from .models import Generaluser
from .models import Journal
from .models import Publication
from .models import Writes
from .models import Belongs
from .models import Quotes
from .resources import *
from import_export.admin import ImportExportModelAdmin
        
class InstitutionAdmin(ImportExportModelAdmin):
    resource_class = InstitutionResource
    list_display = ['institution_id', 'name']

        
class GenerlaluserAdmin(ImportExportModelAdmin):
    resource_class = GeneraluserResource
    list_display = ["general_user_id", "username", "first_name", "last_name",
                    "email", "age", "is_alive", "is_author"]
        
class BelongsAdmin(ImportExportModelAdmin):
    resource_class = BelongsResource
    list_display = ["institution_id", "general_user_id"]
        
class JournalAdmin(ImportExportModelAdmin):
    resource_class = JournalResource
    list_display = ["journal_id", "name"]
        
class PublicationAdmin(ImportExportModelAdmin):
    resource_class = PublicationResource
    list_display = ["publication_id", "journal_id", "title", "publication_date"]
        
class QuotesAdmin(ImportExportModelAdmin):
    resource_class = QuotesResource
    list_display = ["publication_id", "publication_id"]
    
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
admin.site.register(Generaluser,GenerlaluserAdmin)
admin.site.register(Journal,JournalAdmin)
admin.site.register(Publication,PublicationAdmin)
admin.site.register(Writes,WritesAdmin)
admin.site.register(Belongs,BelongsAdmin)
admin.site.register(Quotes,QuotesAdmin)
