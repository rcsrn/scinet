from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Institution
from .models import GeneralUser
from .models import Journal
from .models import Publication
from .models import Writes
from .models import Belongs
from .models import Quotes
from .resources import *
        
class InstitutionAdmin(ImportExportModelAdmin):
    resource_class = InstitutionResource
    list_display = ['institution_id', 'name']

class GenerlaluserAdmin(ImportExportModelAdmin):
    resource_class = GeneraluserResource
    list_display = ["general_user_id", "username", "first_name", "last_name",
                    "email", "password", "age", "is_alive", "is_author"]
        
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
        
class WritesAdmin(ImportExportModelAdmin):
    resource_class = WritesResource
    list_display = ["general_user_id", "publication_id"]

admin.site.register(Institution,InstitutionAdmin)
admin.site.register(GeneralUser,GenerlaluserAdmin)
admin.site.register(Journal,JournalAdmin)
admin.site.register(Publication,PublicationAdmin)
admin.site.register(Writes,WritesAdmin)
admin.site.register(Belongs,BelongsAdmin)
admin.site.register(Quotes,QuotesAdmin)
