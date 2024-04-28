from django.contrib import admin
from .models import Post #import Post class made in models.py

admin.site.register(Post) #register the Post class so the site knows it's legit and people can see it
