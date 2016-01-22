from django.db import models

class clientdata(models.Model):
        class Meta:
                db_table = 'clientdata'
        
        shortDesc = models.CharField(max_length=200)
        name = models.CharField(max_length=200)
        sourceID = models.IntegerField(null=True)

