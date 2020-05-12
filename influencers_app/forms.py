from django import forms
from .models import Influencer


class InfluencerForm(forms.ModelForm):
    """Форма заполнения новго Influenccer"""
    # name = forms.CharField(max_length=100, required=True)
    # channels_url = forms.CharField(max_length=100, required=True)
    # email = forms.CharField(max_length=100, required=True)


    class Meta:
        model = Influencer
        fields = ("name", "channels_url", "email", "responsible")
