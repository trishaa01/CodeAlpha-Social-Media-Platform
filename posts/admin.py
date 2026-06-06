from django.contrib import admin

from .models import (
    Post,
    Like,
    Comment
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'created_at'
    )

    search_fields = (
        'user__username',
        'content'
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'post'
    )

    search_fields = (
        'user__username',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'post',
        'created_at'
    )

    search_fields = (
        'user__username',
        'text'
    )
