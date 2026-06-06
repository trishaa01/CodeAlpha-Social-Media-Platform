from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, Follow, FollowRequest

from posts.models import Post


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile.objects.create(user=user)

            login(request, user)

            return redirect('feed')
    else:
        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


@login_required
def profile_view(request, username):

    profile_user = get_object_or_404(
        User,
        username=username
    )

    profile = profile_user.profile

    is_owner = request.user == profile_user

    is_follower = Follow.objects.filter(
        follower=request.user,
        following=profile_user
    ).exists()

    if profile.is_private and not is_owner and not is_follower:
        posts = []
    else:
        posts = Post.objects.filter(
            user=profile_user
        ).order_by('-created_at')

    followers_count = Follow.objects.filter(
        following=profile_user
    ).count()

    following_count = Follow.objects.filter(
        follower=profile_user
    ).count()

    pending_request = FollowRequest.objects.filter(
        sender=request.user,
        receiver=profile_user
    ).exists()

    context = {
        'profile_user': profile_user,
        'profile': profile,
        'posts': posts,
        'followers_count': followers_count,
        'following_count': following_count,
        'is_owner': is_owner,
        'is_follower': is_follower,
        'pending_request': pending_request,
    }

    return render(
        request,
        'profile.html',
        context
    )


@login_required
def edit_profile(request):

    if request.method == 'POST':

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect(
                'profile',
                username=request.user.username
            )

    else:
        user_form = UserUpdateForm(
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            instance=request.user.profile
        )

    return render(
        request,
        'edit_profile.html',
        {
            'user_form': user_form,
            'profile_form': profile_form
        }
    )


@login_required
def follow_user(request, username):

    target_user = get_object_or_404(
        User,
        username=username
    )

    if target_user == request.user:
        return redirect(
            'profile',
            username=username
        )

    if target_user.profile.is_private:

        FollowRequest.objects.get_or_create(
            sender=request.user,
            receiver=target_user
        )

    else:

        Follow.objects.get_or_create(
            follower=request.user,
            following=target_user
        )

    return redirect(
        'profile',
        username=username
    )


@login_required
def unfollow_user(request, username):

    target_user = get_object_or_404(
        User,
        username=username
    )

    Follow.objects.filter(
        follower=request.user,
        following=target_user
    ).delete()

    return redirect(
        'profile',
        username=username
    )


@login_required
def follow_requests(request):

    requests = FollowRequest.objects.filter(
        receiver=request.user
    )

    return render(
        request,
        'requests.html',
        {'requests': requests}
    )


@login_required
def accept_request(request, request_id):

    follow_request = get_object_or_404(
        FollowRequest,
        id=request_id,
        receiver=request.user
    )

    Follow.objects.get_or_create(
        follower=follow_request.sender,
        following=follow_request.receiver
    )

    follow_request.delete()

    return redirect('follow_requests')


@login_required
def reject_request(request, request_id):

    follow_request = get_object_or_404(
        FollowRequest,
        id=request_id,
        receiver=request.user
    )

    follow_request.delete()

    return redirect('follow_requests')


@login_required
def search_users(request):

    query = request.GET.get('q', '')

    users = User.objects.filter(
        username__icontains=query
    ) if query else []

    return render(
        request,
        'search.html',
        {
            'users': users,
            'query': query
        }
    )
