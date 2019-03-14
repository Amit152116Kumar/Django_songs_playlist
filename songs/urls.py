from django.urls import path
from .views import *
urlpatterns=[
    path('',HomeTemplateView.as_view(),name='home'),
    path('login/',ProfileLoginView.as_view(),name='login'),
    path('logout/', ProfileLogoutView.as_view(), name='logout'),
    path('register/',SignupView.as_view(),name='Register'),
    path('songs/',SongsListView.as_view(),name='songs'),
    path('album/',AlbumListView.as_view(),name='album'),
    path('artists/',ArtistsListView.as_view(),name='artists'),
    path('songs/create/', SongsCreateView.as_view(), name='song-create'),
    path('album/create/', AlbumCreateView.as_view(), name='album-create'),
    path('artists/create/', ArtistsCreateView.as_view(), name='artist-create'),
    path('songs/<int:pk>',SongsDetailView.as_view(),name='song-details'),
    path('album/<int:pk>',AlbumDetailView.as_view(),name='album-details'),
    path('artists/<int:pk>',ArtistsDetailView.as_view(),name='artist-details'),
    path('songs/<int:pk>/delete',SongDeleteView.as_view(),name='song-delete'),
    path('album/<int:pk>/delete',AlbumDeleteView.as_view(),name='album-delete'),
    path('artists/<int:pk>/delete',ArtistDeleteView.as_view(),name='artist-delete'),
    path('songs/<int:pk>/edit/', SongsUpdateView.as_view(), name='song-update'),
    path('album/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album-update'),
    path('artists/<int:pk>/edit/', ArtistsUpdateView.as_view(), name='artist-update'),
    path('profile/<str:username>/',ProfileDetailView.as_view(),name='profile')

]