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

    return render(request, 'index.html', {'topics': topics.values(), 'publications': publications[:6]})

def register(request):
    return render(request, 'register.html')

def topic(request, topic_id):
    topic = Topic.objects.get(topic_id=topic_id)
    publications = Publication.objects.filter(topic=topic_id)
    return render(request, 'topic.html', {'topic': topic, 'publications': publications})

def publication(request, publication_id):
	publication = Publication.objects.get(publication_id=publication_id)
	# id_authors = Writes.objects.filter(publication_id=publication_id).values_list('general_user_id', flat=True)
	# authors = []
	# for id in id_authors:
		# authors.append(GeneralUser.objects.get(general_user_id=id))

	return render(request, 'publication.html', {'publication': publication})


# def user(request, user_id):
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

def login(request):
    return render(request, 'login.html')


# def institution_info(request, insti_id):
# 	institution = Institution.objects.get(institution_id=insti_id)
# 	id_authors = Belongs.objects.filter(institution_id=insti_id).values_list('general_user_id', flat=True)
	
# 	authors = []
# 	for i in id_authors:
# 		authors.append(GeneralUser.objects.get(general_user_id=i))
	
# 	id_publications = []
# 	for id in id_authors:
# 		id_publications.extend(Writes.objects.filter(general_user_id=id).values_list('publication_id', flat=True))
	
# 	publications = []
# 	for id in id_publications:
# 		publications.append(Publication.objects.get(publication_id=id))

	
# 	context = {'institution' : institution, 'publications' : publications, 'authors' : authors}
# 	return render(request , 'institution.html', context)
