from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import NewProjectForm,NewReviewForm,NewProfileForm
from .models import Project,Review,Profile
# Create your views here.

def home(request):
    title = 'awards'
    current_user = request.user
    projects = Project.get_all()
    review = NewReviewForm()
    return render(request, 'index.html',{"projects": projects,"review":review})

def profile(request):
    title = 'awards'
    current_user = request.user
    profile = Profile.objects.filter(user=current_user.id)
    return render(request, 'profile.html',{"profile": profile})

# @login_required(login_url='/accounts/login/')
def NewPost(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save()
            new_post.user = current_user
            new_post.save()
        return redirect('home')

    else:
        form = NewProjectForm()
        review = NewReviewForm()
    return render(request, 'post.html', {"form": form,"review":review})

# @login_required(login_url='/accounts/login/')
def NewReview(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewReviewForm(request.POST, request.FILES)
        if form.is_valid():
            new_review = form.save()
            new_review.user = current_user
            new_review.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'index.html', {"form": form})

def NewProfile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save()
            new_profile.user = current_user
            new_profile.save()
        return redirect('home')

    else:
        profile = NewProfileForm()
    return render(request, 'update.html', {"profile": profile})

# @login_required(login_url='/accounts/login/')
def search_results(request):
                                                                  
    if 'search' in request.GET and request.GET['search']:
        search_item = request.GET.get('search')
        searched_projects = Project.objects.filter(project_title=search_item)
        message = f"{searched_projects}"
        return render(request, 'search.html',{"message":message,"projects": searched_projects})
    else:
        message = "You haven't searched for any projects"
        return render(request, 'search.html',{"message":message})
