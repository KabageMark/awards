from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('^post$',views.NewPost,name = 'post-project'),
    url('^profile$',views.profile,name = 'profile'),
    url('^update$',views.NewProfile,name = 'post-profile'),
    url('^search$',views.search_results,name = 'search-projects'),
    url('^review/(\d+)$', views.review, name='review'),
    url('^api/profilemerch/$', views.ProfileList.as_view()),
    url('^api/projectmerch/$', views.ProjectList.as_view()),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)