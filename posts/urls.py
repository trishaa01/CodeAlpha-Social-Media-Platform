from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.feed,
        name='feed'
    ),

    path(
        'create-post/',
        views.create_post,
        name='create_post'
    ),

    path(
        'delete-post/<int:post_id>/',
        views.delete_post,
        name='delete_post'
    ),

    path(
        'like/<int:post_id>/',
        views.like_post,
        name='like_post'
    ),

    path(
        'unlike/<int:post_id>/',
        views.unlike_post,
        name='unlike_post'
    ),

    path(
        'comment/<int:post_id>/',
        views.add_comment,
        name='add_comment'
    ),

    path(
        'delete-comment/<int:comment_id>/',
        views.delete_comment,
        name='delete_comment'
    ),
]
