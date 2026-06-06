from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['content', 'image', 'video']

        widgets = {
            'content': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': "What's on your mind?",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')

        # At least one of content, image, or video must be provided
        if not content and not image and not video:
            raise forms.ValidationError(
                "Please add some text, a photo, or a video."
            )

        # Cannot upload both image and video at once
        if image and video:
            raise forms.ValidationError(
                "Please upload either a photo or a video, not both."
            )

        return cleaned_data


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ['text']

        widgets = {
            'text': forms.TextInput(
                attrs={
                    'placeholder': 'Add a comment...'
                }
            )
        }
