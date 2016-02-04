from django.db import models
from django.conf import settings
#from movies.model import Movie
from movies.models import Movie
from mofilmuser.models import MofilmUser
from django.contrib.auth.models import User

# Create your models here.

class Portal(models.Model):
    brandID = models.IntegerField()
    createDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)


class PortalProject(models.Model):
    projectID = models.IntegerField()
    name = models.CharField(max_length=100)
    portalID = models.IntegerField()
    createDate = models.DateTimeField(auto_now=True)

class PortalContent(models.Model):
    #movieID = models.IntegerField(default=0)
    movies = models.OneToOneField(Movie,db_column='movies_id')
    portalID = models.IntegerField()
    contentType = models.CharField(max_length=100)
    licenseTerms = models.TextField()
    createDate = models.DateTimeField(auto_now=True)
    someText = "dasdsa"

class PortalUser(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True, )
    userID = models.OneToOneField(User)
    portalID = models.OneToOneField(Portal)


