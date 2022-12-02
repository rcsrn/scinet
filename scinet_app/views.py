from django.shortcuts import render
from .models import Quotes, Publication
import operator

def index(request):
	quotes = Quotes.objects.all()
	cited_publications = {}
	for quote in quotes:
		if quote.publication_id not in cited_publications.keys():
			cited_publications[quote.publication_id] = 1
		else:
			cited_publications[quote.publication_id] += 1

	sorted_publications = sorted(cited_publications.items(), key=operator.itemgetter(1), reverse=True)
	publications = []
	for publication in sorted_publications:
		publications.append(publication[0])

	return render(request, 'index.html', {'most_cited': sorted_publications})