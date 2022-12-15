from django.shortcuts import render
from .models import Publication, GeneralUser, Institution, Topic
import operator

# def index(request):
#     return render(request, 'index.html')

def index(request):
    topics = Topic.objects.all()
    return render(request, 'index.html', {'topics': topics.values()})

def register(request):
    return render(request, 'register.html')

def topic(request, topic_id):
    topic = Topic.objects.get(topic_id=topic_id)
    publications = Publication.objects.filter(topic=topic_id)
    return render(request, 'topic.html', {'topic': topic, 'publications': publications})

# def publication(request, publication_id):
# 	publication = Publication.objects.get(publication_id=publication_id)
# 	id_authors = Writes.objects.filter(publication_id=publication_id).values_list('general_user_id', flat=True)
# 	authors = []
# 	for id in id_authors:
# 		authors.append(GeneralUser.objects.get(general_user_id=id))

# 	return render(request, 'publication.html', {'publication': publication, 'authors': authors})


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
