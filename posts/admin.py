from django.contrib import admin

from .models import (
    Profile,
    Follow,
    FollowRequest
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'is_private'
    )

    search_fields = (
        'user__username',
    )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):

    list_display = (
        'follower',
        'following',
        'created_at'
    )

    search_fields = (
        'follower__username',
        'following__username'
    )


@admin.register(FollowRequest)
class FollowRequestAdmin(admin.ModelAdmin):

    list_display = (
        'sender',
        'receiver',
        'created_at'
    )

    search_fields = (
        'sender__username',
        'receiver__username'
    )
