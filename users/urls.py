from django.conf.urls import url

from . import views

urlpatterns = [
    # View all User
    url(r'^$', views.index, name='index'),

    #Display a form for creating a user
    url(r'^register_start', views.registerStart, name='users.registerStart'),

    # Sign in a user
    url(r'^signin', views.signIn, name='users.signIn'),

    # Logout a user
    url(r'^logout', views.logout, name='users.logout'),

    #View a user profile
    url(r'^profile/(?P<user_id>[0-9]+)$', views.profile, name='users.profile'),

    #Edit a user
    url(r'^edit/(?P<id>[0-9]+)$', views.edit, name='users.editprofile'),
]
