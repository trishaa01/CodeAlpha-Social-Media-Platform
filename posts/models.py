from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)

    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        default='default.jpg',
        blank=True
    )

    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE
    )

    following = models.ForeignKey(
        User,
        related_name='followers',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} follows {self.following}"


class FollowRequest(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='sent_requests',
        on_delete=models.CASCADE
    )

    receiver = models.ForeignKey(
        User,
        related_name='received_requests',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'receiver')

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"
