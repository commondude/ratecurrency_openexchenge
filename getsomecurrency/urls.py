from django.conf.urls import url
from getsomecurrency.views import JsonTalk,GetSome
from . import views


urlpatterns = [
    url(r'^json',JsonTalk.as_view(), name = 'json'),
    url(r'^$',GetSome.as_view(),name = 'getsome' ),

#    url('json',views.jsontalk, name= 'json'),
#    url('', views.getsome, name='getsome'),

]
