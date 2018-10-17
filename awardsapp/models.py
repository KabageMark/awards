from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile-pics')
    bio = models.TextField()
    user = models.ForeignKey(User,null=True)
    contacts = models.CharField(max_length=30)

    @classmethod
    def get_all(cls):
        all_objects = Profile.objects.all()
        return all_objects
     
    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(user__name__icontains=search_term)
        return profile
    @classmethod
    def update_caption(cls,current_value,new_value):
        fetched_object = Image.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

    @classmethod
    def save_profile(self):
        return self.save()

    @classmethod   
    def delete_image(self):
        return self.delete()


class Project(models.Model):
    project_image = models.ImageField(upload_to='projects-images')
    project_title = models.CharField(max_length =30)
    project_description = models.CharField(max_length =30)
    project_link = models.URLField(max_length=128)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    
    @classmethod
    def get_all(cls):
        all_objects = Project.objects.all()
        return all_objects

    @classmethod
    def search_by_name(cls,search_term):
        project = cls.objects.filter(name__icontains=search_term)
        return project

    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result

    @classmethod
    def update_caption(cls,current_value,new_value):
        fetched_object = Image.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

    @classmethod
    def save_image(self):
        return self.save()

    @classmethod    
    def delete_image(self):
        return self.delete()
 
class Review(models.Model):
    user = models.ForeignKey(User,null=True)
    project=models.ForeignKey(Project,related_name='reviews',null=True)
    design=models.IntegerField(max_length=200,null=True)
    usability=models.IntegerField(max_length=200,null=True)
    content=models.IntegerField(max_length=200,null=True)
    



