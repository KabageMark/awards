from django.shortcuts import render
from django.http  import HttpResponse
from .forms import NewProjectForm
# Create your views here.

def welcome(request):
    return render(request, 'index.html')

# @login_required(login_url='/accounts/login/')
def NewPost(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save()
            new_post.user = current_user
            new_post.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'post.html', {"form": form})