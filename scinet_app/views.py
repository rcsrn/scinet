from django.shortcuts import render
from .models import Publication, GeneralUser, Institution, Topic, Citations
import operator

def index(request):
    topics = Topic.objects.all()
    citations = Citations.objects.all()
    cited_publications = {}
    for citation in citations:
        if citation.citee not in cited_publications.keys():
            cited_publications[citation.citee] = 1
        else:
            cited_publications[citation.citee] += 1

    sorted_publications = sorted(cited_publications.items(), key=operator.itemgetter(1), reverse=True)
    publications = []
    for publication in sorted_publications:
        publications.append(publication[0])

    return render(request, 'index.html', {'topics': topics.values(), 'publications': publications[:20]})

def register(request):
    return render(request, 'register.html')

def topic(request, topic_id):
    topic = Topic.objects.get(topic_id=topic_id)
    all_publications = Publication.objects.all()
    publications = []
    for publication in all_publications:
        if topic in publication.topic.all():
            publications.append(publication)
    return render(request, 'topic.html', {'topic': topic, 'publications': publications})

def publication(request, publication_id):
    publication = Publication.objects.get(publication_id=publication_id)
    all_authors = GeneralUser.objects.all()
    authors = []
    for author in all_authors:
        if publication in author.publications.all():
            authors.append(author)

    citation_ids = Citations.objects.values_list('citer', flat=True).filter(citee=publication_id)
    cited_by = []
    for id in citation_ids:
        cited_by.append(Publication.objects.get(publication_id=id))
    return render(request, 'publication.html', {'publication': publication, 'authors': authors, 'cited_by': cited_by})

def user(request, user_id):
    user = GeneralUser.objects.get(general_user_id=user_id)
# 	user = GeneralUser.objects.get(general_user_id=user_id)
# 	id_publications = Writes.objects.filter(general_user_id=user_id).values_list('publication_id', flat=True)
# 	publications = []
# 	for id in id_publications:
# 		publications.append(Publication.objects.get(publication_id=id))
  
# 	id_institutions = Belongs.objects.filter(general_user_id=user_id).values_list('institution_id', flat=True)
# 	institutions = []
# 	for id in id_institutions:
# 		institutions.append(Institution.objects.get(institution_id=id))
# 	return render(request, 'user.html', {'user': user, 'publications': publications, 'institutions': institutions})
    return render(request, 'user.html', {'user': user})

def login(request):
    return render(request, 'login.html')


def institution_info(request, insti_id):
<<<<<<< HEAD
	institution = Institution.objects.get(institution_id=insti_id)
	#id_authors = Belongs.objects.filter(institution_id=insti_id).values_list('general_user_id', flat=True)
	id_authors  = GeneralUser.objects.get(institutions=insti_id)
	authors = []
	for i in id_authors:
		authors.append(GeneralUser.objects.get(general_user_id=i))
=======
 	institution = Institution.objects.get(institution_id=insti_id)
    return render(request, 'institution.html')
# 	id_authors = Belongs.objects.filter(institution_id=insti_id).values_list('general_user_id', flat=True)
>>>>>>> e7bfb3f (Indentation error)
	
	id_publications = []
	for id in id_authors:
		id_publications.extend(Writes.objects.filter(general_user_id=id).values_list('publication_id', flat=True))
	
	publications = []
	for id in id_publications:
		publications.append(Publication.objects.get(publication_id=id))

	
	context = {'institution' : institution, 'publications' : publications, 'authors' : authors}
	return render(request , 'institution.html', context)
