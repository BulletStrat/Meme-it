from django.conf.urls import url
from .views import home, meme_detail, upload_meme

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^meme/(?P<id>\d+)/$', meme_detail, name='detail'),
    url(r'^meme/upload/$', upload_meme, name='upload')
]
