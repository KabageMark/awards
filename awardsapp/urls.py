from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('^post$',views.NewPost,name = 'post-project'),
     url('^update$',views.NewProfile,name = 'post-update'),
    url(r'^review/(\d+)', views.NewReview, name='review'),
    url('^search$',views.search_results,name = 'search-projects'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)