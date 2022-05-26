from django.db import models


# Create your models here.
def attachment_path(instance, filename):
    return 'Arts/' + str(instance.name) + '/attachments/' + filename


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Genre')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Art(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Art Name', help_text='Name')
    TYPE = [
        ('painting', 'Painting'),
        ('sculpture', 'Sculpture'),
        ('digital', 'Digital'),
        ('audio-visual', 'Audio-Visual')
    ]
    type = models.CharField(max_length=100, choices=TYPE, verbose_name='Type of art')
    img = models.ImageField(upload_to=attachment_path, blank=True, null=True, verbose_name='Image')
    year = models.DateField(blank=True, null=True, help_text='datum', verbose_name='Date')
    genres = models.ManyToManyField(Genre, help_text='Genre')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Attachment(models.Model):
    name = models.CharField(max_length=100, verbose_name='atachment title')
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name='file')
    art = models.ForeignKey(Art, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
