#
from django.conf.urls import url
from . import views

urlpatterns = [
   #/appone/
   url(r'^$', views.index, name='index'),
   url(r'^json/$', views.raw, name='json'),
]

