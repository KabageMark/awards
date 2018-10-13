from .models import Project,Profile,Review
from django import forms
#......
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['users']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }