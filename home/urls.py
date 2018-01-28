from django.conf.urls import url

from . import views

urlpatterns = [
    # View all User
    url(r'^$', views.index, name='index'),
]
