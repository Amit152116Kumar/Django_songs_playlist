from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404,get_list_or_404
from .forms import *


class HomeTemplateView(TemplateView):
    template_name = 'home.htm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.request.user.is_authenticated:
            query = self.request.GET.get('q')
            qs = Album.objects.filter(owner=self.request.user.profile)
            if query:
                qs = qs.filter(Q(Title__icontains=query) |
                               Q(song__Title__icontains=query) |
                               Q(song__Artist__Title__icontains=query)).distinct()
            context['album'] = qs
        return context


class SongsListView(LoginRequiredMixin,ListView):
    template_name = 'lists.htm'

    def get_queryset(self):
        return Song.objects.filter(owner=self.request.user.profile)

    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data()
        context['title']='Songs'
        return context


class AlbumListView(LoginRequiredMixin,ListView):
    template_name = 'lists.htm'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user.profile)

    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data()
        context['title']='Album'
        return context


class ArtistsListView(LoginRequiredMixin,ListView):
    template_name = 'lists.htm'

    def get_queryset(self):
        return Artist.objects.filter(owner=self.request.user.profile)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Artists'
        return context


class SongsDetailView(LoginRequiredMixin,DetailView):
    template_name = 'song_details.htm'

    def get_queryset(self):
        return Song.objects.filter(owner=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context



class AlbumDetailView(LoginRequiredMixin,DetailView):
    template_name = 'album_details.htm'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class ArtistsDetailView(LoginRequiredMixin,DetailView):
    template_name = 'artist_details.htm'

    def get_queryset(self):
        return Artist.objects.filter(owner=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class SongsCreateView(LoginRequiredMixin,CreateView):
    template_name ='song_create.htm'
    form_class = SongsCreateForm
    success_url = '/songs/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner=self.request.user.profile
        instance.save()
        return super(SongsCreateView,self).form_valid(form)

    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs['user']=self.request.user.profile
        return kwargs

    def get_queryset(self):
        return Song.objects.filter(owner=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['title']='Create Song'
        return context


class AlbumCreateView(LoginRequiredMixin,CreateView):
    template_name ='album_create.htm'
    form_class = AlbumCreateForm
    success_url = '/album/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner=self.request.user.profile
        instance.save()
        return super(AlbumCreateView,self).form_valid(form)



class ArtistsCreateView(LoginRequiredMixin,CreateView):
    template_name ='artist_create.htm'
    form_class = ArtistCreateForm
    success_url = '/artists/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner=self.request.user.profile
        instance.save()
        return super(ArtistsCreateView,self).form_valid(form)



class SongsUpdateView(LoginRequiredMixin, UpdateView):
    template_name ='song_create.htm'
    form_class = SongsCreateForm
    success_url = '/songs/'

    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs['user']=self.request.user.profile
        return kwargs

    def get_queryset(self):
        return Song.objects.filter(owner=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['title']='Update Song'
        return context


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    template_name ='album_create.htm'
    form_class = AlbumCreateForm
    success_url = '/album/'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user.profile)



class ArtistsUpdateView(LoginRequiredMixin,UpdateView):
    template_name ='artist_create.htm'
    form_class = ArtistCreateForm
    success_url = '/artists/'

    def get_queryset(self):
        return Artist.objects.filter(owner=self.request.user.profile)



class SongDeleteView(DeleteView):
    template_name = 'delete-view.htm'
    success_url = '/songs/'

    def get_queryset(self):
        return Song.objects.filter(owner=self.request.user.profile)


class AlbumDeleteView(DeleteView):
    template_name = 'delete-view.htm'
    success_url = '/album/'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user.profile)


class ArtistDeleteView(DeleteView):
    template_name = 'delete-view.htm'
    success_url = '/artists/'

    def get_queryset(self):
        return Artist.objects.filter(owner=self.request.user.profile)



class ProfileLoginView(LoginView):
        template_name = 'login.htm'
        def get_context_data(self, **kwargs):
            context=super().get_context_data()
            return context


class ProfileLogoutView(LogoutView):
    template_name = 'home.htm'


class SignupView(FormView):
    form_class = UserRegistrationForm
    template_name = 'SignUp.htm'
    success_url = '/'



class ProfileDetailView(LoginRequiredMixin,DetailView):
    template_name = 'profile.htm'

    def get_object(self):
        username=self.kwargs.get("username")
        return get_object_or_404(User,username__iexact=username, is_active=True)

