from django.shortcuts import render
from .models import Quotes, Publication, Writes, GeneralUser, Institution, Belongs
import operator

def index(request):
	quotes = Quotes.objects.all()
	cited_publications = {}
	for quote in quotes:
		if quote.publication_id not in cited_publications.keys():
			cited_publications[quote.publication_id] = 1
		else:
			cited_publications[quote.publication_id] += 1

	sorted_publications = sorted(cited_publications.items(), 
                              key=operator.itemgetter(1), reverse=True)

	return render(request, 'index.html', {'most_cited': sorted_publications})

def register(request):
    return render(request, 'register.html')

def publication(request, publication_id):
	publication = Publication.objects.get(publication_id=publication_id)
	id_authors = Writes.objects.filter(publication_id=publication_id).values_list('general_user_id', flat=True)
	authors = []
	for id in id_authors:
		authors.append(GeneralUser.objects.get(general_user_id=id))

	return render(request, 'publication.html', {'publication': publication, 'authors': authors})


def user(request, user_id):
	user = GeneralUser.objects.get(general_user_id=user_id)
	id_publications = Writes.objects.filter(general_user_id=user_id).values_list('publication_id', flat=True)
	publications = []
	for id in id_publications:
		publications.append(Publication.objects.get(publication_id=id))

	return render(request, 'user.html', {'user': user, 'publications': publications})


def institution_info(request, institution_id):
	institution = Institution.objects.get(institution_id = institution_id)
	id_authors = Belongs.objects.filter(institution_id=institution_id).values_list('general_user_id', flat=True)
	publications = []
	for id in id_authors:
		publications.extend(Writes.objects.filter(general_user_id=id).values_list('publication_id', flat=True))
 
	context = {'institution' : institution, 'publications' : publications, 'authors' : id_authors}
	return render(request , 'institution.html', context)