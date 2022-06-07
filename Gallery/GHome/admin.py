from django.contrib import admin
from .models import Author, Album, Attachment, Genre

# Register your models here.
admin.site.register(Author)
admin.site.register(Album)
admin.site.register(Attachment)
admin.site.register(Genre)