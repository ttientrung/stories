from django.db import models
from django.utils import timezone
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Story(models.Model):
    category = models.ForeignKey(Category, on_delete= models.PROTECT)
    name = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=250)
    url = models.URLField(null=True)
    summary = models.TextField(null=True, blank=True)
    # content = models.TextField(blank=True)
    # content = RichTextField(blank=True)
    content = RichTextUploadingField(blank=True)
    public_day = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='stories/images', default='stories/images/logo.jpg')
    viewed = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)

# Create your models here.
