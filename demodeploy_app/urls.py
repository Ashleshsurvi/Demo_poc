from django.urls import path,include
from django.conf.urls import url
from .views import index,web


urlpatterns = [
    url('index',index.as_view()),
    url('web',web.as_view()),

]
