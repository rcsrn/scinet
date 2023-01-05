from django.core.management import call_command
from django.test import TestCase
from scinet_app.models import Publication

class PublicationsTestCase(TestCase):
    
    #command to run test:
    # ./manage.py test scinet_app.management.commands.test_populate.PublicationsTestCase.all_publications_have_authors
    def all_publications_have_authors(self):
        #first run the command 
        call_command('populate')

        #see if all publications have authors
        publications = []
        publications = Publication.objects.all()
        #size = Publication.objects.all().__len__()
        print("Number of publications: "+str(publications.__len__())+"\n")
        
        for pub in publications:
            if pub.generaluser_set.filter(slug=requested_slug).exists():
                self.assertTrue(True)
            else:
                self.assertTrue(False)
                print(pub.publication_id +'\n')

        
         
# class PublicationTestCase(TestCase):
    
#     def pub_have_authors(self):
#         # publication = Publication.objects.get(publication_id=publication_id)
#         # all_authors = GeneralUser.objects.all()
#         # authors = []
#         # for author in all_authors:
#         #     if publication in author.publications.all():
#         #         authors.append(author)
#         unittest.run(populate)
#         publications = []
#         publications = Publication.objects.all()
        
#         for pub in publications:
#             if pub.generaluser_set.filter(slug=requested_slug).exists():
#                 self.assertTrue(False)

#         #if user.partner_set.filter(slug=requested_slug).exists():
#      # do some private stuff
        
#         # for pub in publications:
#         #     pub.
#         # self.assertTrue(publications)

