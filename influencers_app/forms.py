from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Influencer, VideoInformation


class InfluencerForm(forms.ModelForm):
    """Форма заполнения новго Influenccer"""
    # name = forms.CharField(max_length=100, required=True)
    # channels_url = forms.CharField(max_length=100, required=True)
    # email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = Influencer
        fields = ("name", "channels_url", "email", "responsible")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'table table-bordered '


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.se
        if commit:
            user.save()
        return user


class VideoInformationForm(forms.ModelForm):
    class Meta:
        model = VideoInformation
        fields = ('video_id', 'views_count', 'comments_count', 'likes_count',
                  'dislikes_count')

