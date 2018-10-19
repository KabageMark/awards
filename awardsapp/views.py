from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse
from .forms import NewProjectForm,NewReviewForm,NewProfileForm
from .models import Project,Review,Profile
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projets = Project.objects.all()
        projectserializers = ProjectSerializer(all_projets, many=True)
        return Response(projectserializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        profileserializers = ProfileSerializer(all_profiles, many=True)
        return Response(profileserializers.data)

def home(request):
    title = 'awards'
    current_user = request.user
    review = Review.get_all()
    projects = Project.get_all()
    form = NewReviewForm()
    return render(request, 'index.html',{"projects": projects,"form":form,"review":review})

def review(request,review_id):
    title = 'awards'
    current_user = request.user
    review = get_object_or_404(Project,pk=review_id)
    if request.method == 'POST':
        form = NewReviewForm(request.POST, request.FILES)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.project = review
            new_review.user = current_user
            new_review.save()
        return redirect('home')
    return render(request, 'index.html',{"review":review})

def profile(request):
    title = 'awards'
    current_user = request.user
    profile = Profile.objects.filter(user=current_user.id)
    return render(request, 'profile.html',{"profile": profile})

@login_required(login_url='/accounts/login/')
def NewPost(request):
    title = 'awards'
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

@login_required(login_url='/accounts/login/')
def NewProfile(request):
    title = 'awards'
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

@login_required(login_url='/accounts/login/')
def search_results(request):
    title = 'awards'
                                                                  
    if 'search' in request.GET and request.GET['search']:
        search_item = request.GET.get('search')
        searched_projects = Project.objects.filter(project_title=search_item)
        message = f"{searched_projects}"
        return render(request, 'search.html',{"message":message,"projects": searched_projects})
    else:
        message = "You haven't searched for any projects"
        return render(request, 'search.html',{"message":message})
