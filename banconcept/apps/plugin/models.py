from django.db import models

# Create your models here.

class Plugin(models.Model):
    plugin_name = models.CharField(max_length=200)
	is_published = models.BooleanField()
	created_date = models.DateTimeField('Date Created')
	description = models.TextField()
	slug = models.SlugField(unique=True)