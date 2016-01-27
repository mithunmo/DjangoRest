from django.db import models
from django.conf import settings

# Create your models here.

class Portal(models.Model):
    brandID = models.IntegerField()
    createDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    token = models.CharField(max_length=100)


class PortalProject(models.Model):
    projectID = models.IntegerField()
    portalID = models.IntegerField()
    createDate = models.DateTimeField(auto_now=True)
