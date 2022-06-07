from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('attachments/', views.attachmets, name='attachmet_detail'),
    path('attachments/<slug:slug>/', views.AlbumDetail.as_view(), name='album_detail'),
    path('attachments/author/<slug:slug>', views.AuthorDetail.as_view(), name='author_detail')
]