from django.urls import re_path as url
from blog.views import views

urlpatterns = [
    url(r'view$', views.view),
    url(r'view_list', views.view_list)
]