from django.db import models

# Create your models here.
class MofilmUser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    clientid = models.IntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=70)
    enabled = models.CharField(max_length=1)
    territoryid = models.IntegerField(db_column='territoryID', blank=True, null=True)  # Field name made lowercase.
    facebookid = models.BigIntegerField(db_column='facebookID', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    registered = models.DateTimeField(auto_now=True)
    regip = models.CharField(db_column='regIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(unique=True, max_length=32, blank=True, null=True)
    autocommitstatus = models.IntegerField(db_column='autoCommitStatus', blank=True, null=True)  # Field name made lowercase.
    userrole = models.IntegerField(db_column='userRole')  # Field name made lowercase.
    proenabled = models.IntegerField(db_column='proEnabled')  # Field name made lowercase.
    proonly = models.IntegerField(db_column='proOnly')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
