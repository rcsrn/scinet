from sqlite3 import IntegrityError
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Institution
from .models import GeneralUser
from .models import Journal
from .models import Publication
from .models import Topic
from .models import Citations
from .resources import *
        
class InstitutionAdmin(ImportExportModelAdmin):
    resource_class = InstitutionResource
    list_display = ['institution_id', 'name', 'creation_date', 'country']

class GenerlaluserAdmin(ImportExportModelAdmin):
    resource_class = GeneraluserResource
    list_display = ["general_user_id", "username", "first_name", "last_name",
                    "email", "password", "age"]
        
class JournalAdmin(ImportExportModelAdmin):
    resource_class = JournalResource
    list_display = ["journal_id", "name"]
        
class PublicationAdmin(ImportExportModelAdmin):
    resource_class = PublicationResource
    list_display = ["publication_id", "journal_id", "title", "publication_date", 
                    'content', 'doi']

class CitationsAdmin(ImportExportModelAdmin):
    resource_class = CitationsResource
    list_display = ["citer", "cited"]
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except IntegrityError as e:
            print('found integrity error')
    


class TopicAdmin(ImportExportModelAdmin):
    resource_class = TopicResource
    list_display = ["topic_id", "name"]


    
admin.site.register(Institution,InstitutionAdmin)
admin.site.register(GeneralUser,GenerlaluserAdmin)
admin.site.register(Journal,JournalAdmin)
admin.site.register(Publication,PublicationAdmin)
admin.site.register(Citations, CitationsAdmin)
admin.site.register(Topic, TopicAdmin)