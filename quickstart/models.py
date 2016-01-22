from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.

class movies(models.Model):
        class Meta:
                db_table = 'movies'

        shortDesc = models.CharField(max_length=200)
        productionYear = models.CharField(max_length=4)
        longDesc = models.TextField()
        moderatorComments = models.TextField(null=True)
        uploaded = models.DateTimeField('date published')
        modified = models.DateTimeField('date published')
        moderated = models.DateTimeField('date published',null=True)
        userID = models.IntegerField(default=0)
        private = models.IntegerField(default=0)
        avgRating = models.IntegerField(default=0)
        ratingCount = models.IntegerField(default=0)
        runtime = models.IntegerField(default=0)
        moderatorID = models.IntegerField(null=True)
        status  = models.CharField(max_length=100)
        active  = models.CharField(max_length=100)
        credits  = models.CharField(max_length=100)
        #question = models.ForeignKey(Question)
        anotherT = "dasds"
        def __unicode__(self):
                return self.shortDesc


class sources(models.Model):
	class Meta:
		db_table = "sources"

	#sourceObj = models.ForeignKey(movieSources, related_name="sources", db_column="id", primary_key=True)
	eventID = models.IntegerField(db_column="eventID")
	brandID = models.IntegerField(db_column="brandID")
	sponsorID = models.IntegerField(db_column="sponsorID")
	termsID = models.IntegerField(db_column="termsID")
	tripBudget = models.IntegerField(db_column="tripBudget")
	name = models.CharField(max_length=40)
	webfilename = models.CharField(max_length=50)
	status = models.CharField(max_length=50)
	hidden = models.CharField(max_length=50)
	custom = models.CharField(max_length=50)
	instructions = models.TextField()
	bgcolor = models.CharField(max_length=10)
	startDate =  models.DateTimeField('date published') 
	endDate =  models.DateTimeField('date published')
	closeDate = models.DateField()
	createdDate = models.DateTimeField()
        
		

class movieSources(models.Model):

        class Meta:
                db_table = "movieSources"
        movieID = models.ForeignKey(movies, related_name="movieSources", db_column="movieID", primary_key=True)
        sourceID = models.ForeignKey(sources, related_name="movieSources",db_column='sourceID',primary_key=True)


        def __unicode__(self):
                #return ( self.sourceID)
                #return str(self.sourceID.eventID)
		#return '%s : %s' % (self.sourceID.id, self.sourceID.eventID)
		#return ','.join([str(self.sourceID.id), str(self.sourceID.eventID)])
		        return "Event: %s" %(self.sourceID.eventID) + "," + "Source: %s" % (self.sourceID.id)


# Create your models here.

