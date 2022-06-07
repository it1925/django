from django.db import models
# from django.urls import reverse_lazy
# from django.urls import reverse
from django.utils.timezone import now


# Create your models here.


def attachment_path_author(instance ,filename):
    return 'Authors/' + str(instance.name) + '/image/' + filename


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    date_of_creation = models.DateField(default=now)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=attachment_path_author)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def snippet(self):
        return self.text[:100]


def attachment_path_album(instance ,filename):
    return 'Albums/' + str(instance) + '/cover/' + filename


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Genre name',
                            help_text='Enter a film genre (e.g. sci-fi, comedy)')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(unique=True, max_length=50, blank=True)
    date_of_creation = models.DateField(default=now)
    text = models.TextField()
    cover = models.ImageField(upload_to=attachment_path_album)

    genres = models.ManyToManyField(Genre, help_text='Select a genre for this Album')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def snippet(self):
        return self.text[:25] + '...'

    def get_absolute_url(self):
            return reverse("article_detail", kwargs={"slug": self.slug})


def attachment_path_attachment(instance ,filename):
    return 'Albums/' + str(instance.album.name) + '/attachments/' + filename


class Attachment(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)
    date_of_addition = models.DateField(default=now)
    TYPE = (
        ('Img', 'Image'),
        ('Gif', 'Gif'),
        ('Video', 'video'),
    )
    type = models.CharField(max_length=5, choices=TYPE, blank=True)
    file = models.FileField(upload_to=attachment_path_attachment)

    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name