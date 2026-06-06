from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [

    path(
        'register/',
        views.register_view,
        name='register'
    ),

    path(
        'login/',
        LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    path(
        'profile/<str:username>/',
        views.profile_view,
        name='profile'
    ),

    path(
        'edit-profile/',
        views.edit_profile,
        name='edit_profile'
    ),

    path(
        'follow/<str:username>/',
        views.follow_user,
        name='follow_user'
    ),

    path(
        'unfollow/<str:username>/',
        views.unfollow_user,
        name='unfollow_user'
    ),

    path(
        'follow-requests/',
        views.follow_requests,
        name='follow_requests'
    ),

    path(
        'accept-request/<int:request_id>/',
        views.accept_request,
        name='accept_request'
    ),

    path(
        'reject-request/<int:request_id>/',
        views.reject_request,
        name='reject_request'
    ),

    path(
        'search/',
        views.search_users,
        name='search_users'
    ),
]
