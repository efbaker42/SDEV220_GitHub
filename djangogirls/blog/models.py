from django.conf import settings #import settings
from django.db import models #import model structures
from django.utils import timezone #import timezone utility


class Post(models.Model): #class for a blog post, not to be confused with POST method in CRUD APIs
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #I can make really long titles!
    text = models.TextField() #note empty parentheses in this case means there is no max length
    created_date = models.DateTimeField(default=timezone.now) #created date/time is when content is posted
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now() #published_date is when content is posted
        self.save()

    def __str__(self):
        return self.title #if successful, title will display