from django.core.management import call_command
from django.test import TestCase
from scinet_app.models import Publication, GeneralUser

class PublicationsTestCase(TestCase):
    
    #command to run test:
    # ./manage.py test scinet_app.management.commands.test_populate.PublicationsTestCase.all_publications_have_authors
    def all_publications_have_authors(self):
        #first run the command 
        call_command('populate')

        #see if all publications have authors
        publications = []
        publications = Publication.objects.all()

        authors = []
        authors = GeneralUser.objects.all()

        for publication in publications:
            for author in authors:
                if author.publications.filter(publication_id=publication.publication_id).exists():
                    self.assertTrue(True)
                    break
                else:
                    print(str(publication.publication_id )+"\n")
                    self.assertTrue(False)
                    break

        

        
         
