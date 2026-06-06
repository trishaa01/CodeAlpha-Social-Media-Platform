from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import Post, Like, Comment
from .forms import PostForm, CommentForm


@login_required
def feed(request):

    posts = Post.objects.all().order_by(
        '-created_at'
    )

    comment_form = CommentForm()

    return render(
        request,
        'feed.html',
        {
            'posts': posts,
            'comment_form': comment_form
        }
    )


@login_required
def create_post(request):

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            post = form.save(
                commit=False
            )

            post.user = request.user

            post.save()

            return redirect('feed')

    else:

        form = PostForm()

    return render(
        request,
        'create_post.html',
        {'form': form}
    )


@login_required
def delete_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    if post.user == request.user:
        post.delete()

    return redirect('feed')


@login_required
def like_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    return redirect('feed')


@login_required
def unlike_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    Like.objects.filter(
        user=request.user,
        post=post
    ).delete()

    return redirect('feed')


@login_required
def add_comment(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    if request.method == 'POST':

        form = CommentForm(
            request.POST
        )

        if form.is_valid():

            comment = form.save(
                commit=False
            )

            comment.user = request.user
            comment.post = post

            comment.save()

    return redirect('feed')


@login_required
def delete_comment(request, comment_id):

    comment = get_object_or_404(
        Comment,
        id=comment_id
    )

    comment_owner = (
        comment.user == request.user
    )

    post_owner = (
        comment.post.user == request.user
    )

    if comment_owner or post_owner:
        comment.delete()

    return redirect('feed')
