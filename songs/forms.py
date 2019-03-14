from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import *

class SongsCreateForm(forms.ModelForm):
    class Meta:
        model = Song
        fields =[
            'Title','Album','Artist','Lyrics','Duration',
        ]
    def __init__(self,user=None,*args,**kwargs):
        super(SongsCreateForm,self).__init__(*args,**kwargs)
        self.fields['Album'].queryset       = Album.objects.filter(owner=user)
        self.fields['Artist'].queryset      = Artist.objects.filter(owner=user)


class AlbumCreateForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = [
            'Title','Released_on','Cover'
        ]


class ArtistCreateForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'Title'
        ]


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Image']
