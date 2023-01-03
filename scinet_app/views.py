from django.shortcuts import render, redirect
import operator
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth
from django.contrib.auth.forms import AuthenticationForm

from .models import Publication, GeneralUser, Institution, Topic, Citations
from .forms import NewUserForm



def index(request):
    topics = Topic.objects.all()
    citations = Citations.objects.all()
    cited_publications = {}
    for citation in citations:
        if citation.citee not in cited_publications.keys():
            cited_publications[citation.citee] = 1
        else:
            cited_publications[citation.citee] += 1

    sorted_publications = sorted(
        cited_publications.items(), key=operator.itemgetter(1), reverse=True)
    publications = []
    for publication in sorted_publications:
        publications.append(publication[0])

    return render(request, 'index.html', {'topics': topics.values(), 'publications': publications[:20]})

def search(request):
    publications = Publication.objects.filter(title=request.GET.get('search'))
    return render(request, {'publications': publications})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'register.html', {"register_form":form})

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

    citation_ids = Citations.objects.values_list(
        'citer', flat=True).filter(citee=publication_id)
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
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(index)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form":form})

def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully loged out.")
    return redirect("index")

def institution_info(request, insti_id):
    institution = Institution.objects.get(institution_id=insti_id)
    authors = GeneralUser.objects.filter(institutions=insti_id)
    publications = []
    for i in authors:
        publications.extend(i.publications.all())

    # publications = []
    # for id in publications_id:
    #     publications.append(Publication.objects.get(publication_id=id))

    context = {'institution': institution,
               'publications': publications, 'authors': authors}
    return render(request, 'institution.html', context)
