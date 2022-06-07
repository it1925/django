from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.urls import reverse
from .models import Author, Album, Attachment
from django.views.generic import ListView, DetailView


# Create your views here.

def index(request):
    album = Album.objects.all()
    return render(request, 'index.html', context={'albums': album})


def attachmets(request):
    attachment = Attachment.objects.all().order_by('album')
    return render(request, 'album/attachmet_detail.html', context={'attachments': attachment})


class AlbumDetail(DetailView):
    model = Album
    context_object_name = 'album_detail'
    template_name = 'album/album_detail.html'
    # def get_success_url(self):
    #     return reverse('detail', kwargs={'slug': self.object.slug})


class AuthorDetail(ListView):
    model = Author
    context_object_name = 'author_detail'
    template_name = 'author/author.html'
