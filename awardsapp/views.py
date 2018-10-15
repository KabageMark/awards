from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import NewProjectForm
from .models import Project
# Create your views here.

def home(request):
    title = 'awards'
    current_user = request.user
    projects = Project.get_all()
    return render(request, 'index.html',{"projects": projects,})


# @login_required(login_url='/accounts/login/')
def NewPost(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save()
            new_post.user = current_user
            new_post.save()
        return redirect('welcome')

    else:
        form = NewProjectForm()
    return render(request, 'post.html', {"form": form})