from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django_select2 import forms as s2forms

from .models import Influencer, VideoInformation, Content, \
    InfluencersInformation, Shipment


class InfluencerForm(forms.ModelForm):
    """Форма заполнения новго Influenccer"""

    class Meta:
        model = Influencer
        fields = ("name", "channels_url", "email", "responsible")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'table table-bordered '


class InfluencersInformationForm(forms.ModelForm):
    """Форма для обновления и создания полной информации об инфлуенсере"""
    class Meta:
        model = InfluencersInformation
        fields = '__all__'

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


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'table table-bordered '


class ProductWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "sku__icontains",
        "product_name__icontains",
    ]


class ShipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = '__all__'
        widgets = {
            "product": ProductWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'table table-bordered '


class VideoInformationForm(forms.ModelForm):
    class Meta:
        model = VideoInformation
        fields = ('video_id', 'views_count', 'comments_count', 'likes_count',
                  'dislikes_count')
