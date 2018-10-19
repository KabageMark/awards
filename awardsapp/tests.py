from django.test import TestCase
from .models import Profile,Project,Review
from django.contrib.auth.models import User
# Create your tests here.


class UserTest(TestCase):
    def setUp(self):
        self.user=User(username='kabagemark',first_name='mark',last_name='kabage',email='kabagemark@gmail.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
    
    def test_data(self):
        self.assertTrue(self.user.username,"kabagemarl")
        self.assertTrue(self.user.first_name,"mark")
        self.assertTrue(self.user.last_name,'kabage')
        self.assertTrue(self.user.email,'kabagemark@gmail.com')
    
    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)
    
    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)==0)


class ProfileTest(TestCase):
    def setUp(self):
        self.new_user=User(username='markabage',first_name='mark',last_name='kabage',email='kabagemark@gmail.com')
        self.new_user.save()
        self.new_profile=Profile(user=self.new_user,contacts ="0796872516",bio='i love technology')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    
    def test_data(self):
        self.assertTrue(self.new_profile.bio,"i love technology")
        self.assertTrue(self.new_profile.user,self.new_user)

    def test_save(self):
        self.new_profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    
    def test_delete(self):
        profile = Profile.objects.filter(id=1)
        profile.delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)

    
    def test_edit_profile(self):
        self.new_profile.save()
        self.update_profile = Profile.objects.filter(bio='i love technology').update(bio = 'i love technology')
        self.updated_profile = Profile.objects.get(bio='i love technology')
        self.assertTrue(self.updated_profile.bio,'i love technology')





class projectTest(TestCase):
    def setUp(self):
        self.user=User(username='kabagemark',first_name='mark',last_name='kabage',email='kabagemark@gmail.com')
        self.user.save()
        self.new_profile=Profile(user=self.user,contacts="0796872516",bio='i love technology')
        self.new_profile.save()
        self.new_post = Project(user=self.user, project_link="https://www.google.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Project))
    
    def test_data(self):
        self.assertTrue(self.new_post. project_link,"https://www.google.com")
        
    def test_save(self):
        self.new_post.save()
        posts = Project.objects.all()
        self.assertTrue(len(posts)>0)
    
    def test_delete(self):
        post = Project.objects.filter(id=1)
        post.delete()
        posts = Project.objects.all()
        self.assertTrue(len(posts)==0)

    def test_update_post(self):
        self.new_post.save()
        self.update_post = Project.objects.filter(project_link='https://www.google.com').update(project_link = 'https://www.instadk.com')
        self.updated_post = Project.objects.get(project_link='https://www.instadk.com')
        self.assertTrue(self.updated_post.project_link,'https://www.instadk.com')
