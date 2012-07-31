from django.db import models

# Create your models here.

class Plugin(models.Model):
    plugin_name = models.CharField(max_length=200)
	is_published = models.BooleanField()
	created_date = models.DateTimeField('Date Created')
	description = models.TextField()
    owner = models.ForeignKey(User, related_name='+')
	slug = models.SlugField(unique=True)
	
class Build(models.Model):
    build_title = models.CharField(max_length=50)
	is_published = models.BooleanField()
	
class Comment(models.Model):
    comment_user = models.ForeignKey(User, related_name='+')
	comment = models.TextField(max_length=1000)
	
class Artifact(models.Model):
	
	upload_location = '/tmp/bin/fuck/if/i/know'

	plugin = models.ForeignKey(Plugin)
	build_no = models.CharField(max_length=10)
	description = models.TextField()
	changelog = models.TextField()
	artifact_location = models.FileField(upload_to=upload_location)
	is_published = models.BooleanField()