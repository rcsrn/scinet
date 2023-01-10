from django.shortcuts import render, redirect
import operator
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth
from django.contrib.auth.forms import AuthenticationForm

from .models import Publication, GeneralUser, Institution, Topic, Citations
from .forms import NewUserForm, NewResearcherForm, NewPublicationForm

def index(request):
    users = []
    username = request.user.username
    isResearcher = GeneralUser.objects.filter(username=username).count() > 0

    if request.user.is_authenticated and isResearcher:
        users.append(GeneralUser.objects.filter(username=request.user.username))
        
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

    return render(request, 'index.html', {'topics': topics.values(), 'publications': publications[:20], 'users':users},)

def search(request):
    searched = request.GET.get('search')
    if searched == "":
        return index(request)
    
    publications = Publication.objects.filter(title__icontains = searched)
    return render(request, 'search.html', {'publications': publications})

def register(request):
    form = NewUserForm(request.POST or None)
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
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
    return render(request, 'user.html', {'user': user})


def newResearcher(request):
    if request.method == "POST":
        form = NewResearcherForm(request.POST, initial = {'username':request.user.username})
        if form.is_valid():
            researcher = form.save(commit=False)
            researcher.general_user_id = GeneralUser.objects.all().count() + 1
            researcher.save()
            form.save()
            messages.success(request, "You have successfully become researcher")
            return redirect(index)
        else:
            messages.error(request, "The username already exists")
    else:
        form = NewResearcherForm(initial={'username': request.user.username})
    return render(request,'researcher_form.html', {'form': form})


def newPublication(request):
    if request.method == "POST":
        form = NewPublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.publication_id = Publication.objects.all().count() + 1
            publication.save()
            user = GeneralUser.objects.get(username=request.user.username)
            user.publications.add(publication)
            user.save()
            form.save()
            messages.success(request, "Your publication has been uploaded")
            return redirect(index)
        else:
            messages.error(request, "The publication could not be uploaded")
    else:
        form = NewPublicationForm()
    return render(request,'publication_form.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
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

    pub_num = []
    for i in authors:
        pub_num.append(i.publications.count())

    authors_publications = zip(authors, pub_num)
    context = {'institution': institution,
               'publications': publications, 
               'authors': authors, 
               'pub_num': pub_num,
               'iterateOver': range(len(authors)),
               'authors_publications': authors_publications}
    return render(request, 'institution.html', context)

def featured(request):
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
        
    return render(request, 'featured.html', {'publications': publications[:20]})
