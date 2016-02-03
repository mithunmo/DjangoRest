# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Assetdownloadq(models.Model):
    assetid = models.IntegerField(db_column='assetID', primary_key=True)  # Field name made lowercase.
    scheduled = models.DateTimeField()
    tries = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assetDownloadQ'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class BrandDetails(models.Model):
    brandid = models.IntegerField()
    status = models.IntegerField()
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brand_details'


class Brands(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=32, blank=True, null=True)
    company = models.CharField(max_length=32, blank=True, null=True)
    corporateid = models.IntegerField(db_column='corporateID')  # Field name made lowercase.
    industryid = models.IntegerField(db_column='industryID')  # Field name made lowercase.
    firstname = models.CharField(max_length=32, blank=True, null=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    country = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField()
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brands'


class Brands1(models.Model):
    name = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    email = models.CharField(unique=True, max_length=32)
    phone = models.CharField(max_length=20)
    status = models.IntegerField()
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brands1'


class Bulkjobs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    datetime = models.DateTimeField()
    count = models.IntegerField()
    description = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=10)
    filename = models.TextField()
    systemresult = models.TextField(db_column='systemResult', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bulkJobs'


class Bulkmovies(models.Model):
    bulkid = models.IntegerField(db_column='bulkID')  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bulkMovies'
        unique_together = (('bulkID', 'movieID'),)


class Bulkusers(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    ftpdir = models.CharField(db_column='ftpDir', max_length=50)  # Field name made lowercase.
    username = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'bulkUsers'


class Categories(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.
    description = models.CharField(max_length=40)
    exclusive = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'categories'


class Channels(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    link = models.TextField()
    description = models.TextField()
    updatedate = models.DateTimeField(db_column='updateDate')  # Field name made lowercase.
    name = models.CharField(max_length=32)
    category = models.TextField()

    class Meta:
        managed = False
        db_table = 'channels'


class Clientsources(models.Model):
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientSources'
        unique_together = (('clientID', 'sourceID'),)


class Clients(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clients'


class Cohort(models.Model):
    mm = models.IntegerField()
    yy = models.IntegerField()
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    type = models.CharField(max_length=50)
    signup = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cohort'


class Community(models.Model):
    year = models.IntegerField()
    month = models.TextField()
    count = models.IntegerField()
    type = models.TextField()

    class Meta:
        managed = False
        db_table = 'community'


class Contributorroles(models.Model):
    contributorid = models.IntegerField(db_column='contributorID')  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contributorRoles'
        unique_together = (('contributorID', 'roleID'),)


class Contributors(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    photo = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contributors'


class Corporate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=200)
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corporate'


class Currencies(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=50)
    isocodestring = models.CharField(db_column='isoCodeString', max_length=3)  # Field name made lowercase.
    isocodenumeric = models.SmallIntegerField(db_column='isoCodeNumeric')  # Field name made lowercase.
    symbol = models.CharField(max_length=5)
    position = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'currencies'


class Currencyrate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    currencyid = models.IntegerField(db_column='currencyID')  # Field name made lowercase.
    rate = models.FloatField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'currencyRate'


class Datanames(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'datanames'


class Distribution(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=32)
    class_field = models.TextField(db_column='class')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'distribution'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Downloaddata(models.Model):
    downloadid = models.IntegerField(db_column='downloadID')  # Field name made lowercase.
    dataname = models.CharField(db_column='dataName', max_length=30)  # Field name made lowercase.
    datavalue = models.TextField(db_column='dataValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'downloadData'
        unique_together = (('downloadID', 'dataName'),)


class Downloadfiles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    modified = models.DateTimeField()
    description = models.CharField(max_length=40)
    filetype = models.CharField(max_length=10)
    sourceid = models.IntegerField(db_column='sourceID', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField()
    lang = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'downloadFiles'


class Downloadsources(models.Model):
    downloadid = models.IntegerField(db_column='downloadID')  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.
    downloadhash = models.CharField(db_column='downloadHash', unique=True, max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'downloadSources'
        unique_together = (('downloadID', 'sourceID'),)


class Events(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=40)
    webpath = models.TextField(blank=True, null=True)
    hidden = models.CharField(max_length=1)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    awardstartdate = models.DateTimeField(blank=True, null=True)
    awardenddate = models.DateTimeField(blank=True, null=True)
    termsid = models.IntegerField(db_column='termsID', blank=True, null=True)  # Field name made lowercase.
    instructions = models.TextField(blank=True, null=True)
    custom = models.CharField(max_length=1)
    bgcolor = models.CharField(max_length=10, blank=True, null=True)
    tba = models.CharField(max_length=1)
    status = models.CharField(max_length=9)
    productid = models.IntegerField(db_column='productID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'events'


class Events1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=40)
    webpath = models.TextField(blank=True, null=True)
    hidden = models.CharField(max_length=1)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    awardstartdate = models.DateTimeField()
    awardenddate = models.DateTimeField()
    termsid = models.IntegerField(db_column='termsID', blank=True, null=True)  # Field name made lowercase.
    instructions = models.TextField(blank=True, null=True)
    custom = models.CharField(max_length=1)
    bgcolor = models.CharField(max_length=10, blank=True, null=True)
    tba = models.CharField(max_length=1)
    status = models.CharField(max_length=9)
    productid = models.IntegerField(db_column='productID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'events1'


class Events2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=40)
    webpath = models.TextField(blank=True, null=True)
    hidden = models.CharField(max_length=1)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    awardstartdate = models.DateTimeField(blank=True, null=True)
    awardenddate = models.DateTimeField(blank=True, null=True)
    termsid = models.IntegerField(db_column='termsID', blank=True, null=True)  # Field name made lowercase.
    instructions = models.TextField(blank=True, null=True)
    custom = models.CharField(max_length=1)
    bgcolor = models.CharField(max_length=10, blank=True, null=True)
    tba = models.CharField(max_length=1)
    status = models.CharField(max_length=9)
    productid = models.IntegerField(db_column='productID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'events2'


class Eventsdata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    description = models.TextField()
    hash = models.CharField(max_length=32)
    lang = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'eventsData'


class Eventsdata1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    description = models.TextField()
    hash = models.CharField(max_length=32)
    lang = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'eventsData1'


class EventsBack(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=40)
    webpath = models.TextField(blank=True, null=True)
    hidden = models.CharField(max_length=1)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    awardstartdate = models.DateTimeField()
    awardenddate = models.DateTimeField()
    termsid = models.IntegerField(db_column='termsID', blank=True, null=True)  # Field name made lowercase.
    instructions = models.TextField(blank=True, null=True)
    custom = models.CharField(max_length=1)
    bgcolor = models.CharField(max_length=10, blank=True, null=True)
    tba = models.CharField(max_length=1)
    status = models.CharField(max_length=9)
    productid = models.IntegerField(db_column='productID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'events_back'


class Filmgenres(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'filmGenres'


class Grants(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate')  # Field name made lowercase.
    currencysymbol = models.CharField(db_column='currencySymbol', max_length=3)  # Field name made lowercase.
    totalgrants = models.FloatField(db_column='totalGrants')  # Field name made lowercase.
    minimumgrants = models.IntegerField(db_column='minimumGrants', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'grants'


class Grantsdata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    grantid = models.IntegerField(db_column='grantID')  # Field name made lowercase.
    paramname = models.CharField(db_column='paramName', max_length=100)  # Field name made lowercase.
    paramvalue = models.CharField(db_column='paramValue', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grantsData'


class Halloffame(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'halloffame'


class Languages(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField()
    iso = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'languages'


class MmBrandmessages(models.Model):
    brandrepid = models.IntegerField(db_column='brandRepID')  # Field name made lowercase.
    messageid = models.IntegerField(db_column='messageID')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectID')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mm_brandMessages'


class MmMessages(models.Model):
    subject = models.TextField()
    body = models.TextField()
    attachment = models.CharField(max_length=32)
    to = models.CharField(max_length=32)
    from_field = models.CharField(db_column='from', max_length=32)  # Field renamed because it was a Python reserved word.
    html = models.IntegerField()
    status = models.IntegerField()
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mm_messages'


class MmPrivatemessages(models.Model):
    subject = models.CharField(max_length=32)
    body = models.TextField()
    attachment = models.CharField(max_length=32)
    touserid = models.IntegerField(db_column='toUserID')  # Field name made lowercase.
    fromuserid = models.IntegerField(db_column='fromUserID')  # Field name made lowercase.
    messageid = models.IntegerField(db_column='messageID')  # Field name made lowercase.
    read = models.IntegerField()
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mm_privatemessages'


class MmProjectinvitations(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectID')  # Field name made lowercase.
    brandrepid = models.IntegerField(db_column='brandRepID')  # Field name made lowercase.
    status = models.IntegerField()
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mm_projectInvitations'
        unique_together = (('userID', 'projectID'),)


class MmProjectmessages(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    brandrepid = models.IntegerField(db_column='brandRepID')  # Field name made lowercase.
    messageid = models.IntegerField(db_column='messageID')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectID')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mm_projectMessages'


class MmTemplates(models.Model):
    subject = models.TextField()
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'mm_templates'


class MmUsermessages(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    messageid = models.IntegerField(db_column='messageID')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectID')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mm_userMessages'


class Movieasset1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    type = models.CharField(max_length=9)
    ext = models.CharField(max_length=8)
    profileid = models.BigIntegerField(db_column='profileID')  # Field name made lowercase.
    description = models.CharField(max_length=30)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    metadata = models.TextField()
    filename = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    cdnurl = models.TextField(db_column='cdnURL', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movieAsset1'


class Movieasset2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    type = models.CharField(max_length=9)
    ext = models.CharField(max_length=8)
    profileid = models.BigIntegerField(db_column='profileID')  # Field name made lowercase.
    description = models.CharField(max_length=30)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    metadata = models.TextField()
    filename = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    cdnurl = models.TextField(db_column='cdnURL', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movieAsset2'


class Movieassets(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    type = models.CharField(max_length=9)
    ext = models.CharField(max_length=8)
    profileid = models.BigIntegerField(db_column='profileID')  # Field name made lowercase.
    description = models.CharField(max_length=30)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    metadata = models.TextField()
    filename = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    cdnurl = models.TextField(db_column='cdnURL', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movieAssets'


class Movieawards(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.
    position = models.IntegerField()
    type = models.CharField(max_length=11)
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'movieAwards'


class Moviebroadcast(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID')  # Field name made lowercase.
    broadcastdate = models.DateTimeField(db_column='broadCastDate')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movieBroadcast'
        unique_together = (('movieID', 'CountryID'),)


class Moviecategories(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movieCategories'
        unique_together = (('movieID', 'categoryID'),)


class Moviechannel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID', unique=True)  # Field name made lowercase.
    channelid = models.IntegerField(db_column='channelID')  # Field name made lowercase.
    distributionid = models.IntegerField(db_column='distributionID')  # Field name made lowercase.
    width = models.IntegerField()
    height = models.IntegerField()
    bitrate = models.BigIntegerField()
    duration = models.BigIntegerField()
    size = models.BigIntegerField()
    status = models.IntegerField()
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    action = models.TextField()
    category = models.TextField()

    class Meta:
        managed = False
        db_table = 'movieChannel'


class Moviecomments(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    timestamp = models.DateTimeField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'movieComments'


class Moviecontributors(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    contributorid = models.IntegerField(db_column='contributorID')  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movieContributors'
        unique_together = (('movieID', 'contributorID', 'roleID'),)


class Moviedata(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    datanameid = models.IntegerField(db_column='datanameID')  # Field name made lowercase.
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'movieData'
        unique_together = (('movieID', 'datanameID'),)


class Movieedithistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    timestamp = models.DateTimeField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'movieEditHistory'


class Movielanguages(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    languageid = models.IntegerField(db_column='languageID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movieLanguages'
        unique_together = (('movieID', 'languageID'),)


class Movielicenses(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    licenseid = models.IntegerField(db_column='licenseID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movieLicenses'


class Moviemessagehistory(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    messageid = models.IntegerField(db_column='messageID')  # Field name made lowercase.
    senderid = models.IntegerField(db_column='senderID')  # Field name made lowercase.
    recipientid = models.IntegerField(db_column='recipientID')  # Field name made lowercase.
    senddate = models.DateTimeField(db_column='sendDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movieMessageHistory'
        unique_together = (('movieID', 'messageID'),)


class Movieratings(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'movieRatings'
        unique_together = (('movieID', 'userID'),)


class Moviescripts(models.Model):
    projecthash = models.CharField(max_length=32)
    grantid = models.IntegerField(db_column='grantID')  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'movieScripts'


class Moviesources(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movieSources'
        unique_together = (('movieID', 'sourceID'),)


class Movietags(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    tagid = models.IntegerField(db_column='tagID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movieTags'
        unique_together = (('movieID', 'tagID'),)


class Movietracks(models.Model):
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    downloadid = models.IntegerField(db_column='downloadID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movieTracks'
        unique_together = (('movieID', 'downloadID'),)


class Movies(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    status = models.CharField(max_length=15)
    active = models.CharField(max_length=1)
    private = models.IntegerField()
    shortdesc = models.TextField(db_column='shortDesc')  # Field name made lowercase.
    longdesc = models.TextField(db_column='longDesc', blank=True, null=True)  # Field name made lowercase.
    credits = models.CharField(max_length=255)
    runtime = models.IntegerField(blank=True, null=True)
    productionyear = models.CharField(db_column='productionYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    uploaded = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    moderated = models.DateTimeField(blank=True, null=True)
    moderatorid = models.IntegerField(db_column='moderatorID', blank=True, null=True)  # Field name made lowercase.
    moderatorcomments = models.TextField(db_column='moderatorComments', blank=True, null=True)  # Field name made lowercase.
    avgrating = models.IntegerField(db_column='avgRating', blank=True, null=True)  # Field name made lowercase.
    ratingcount = models.IntegerField(db_column='ratingCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movies'


class Movies1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    status = models.CharField(max_length=15)
    active = models.CharField(max_length=1)
    private = models.IntegerField()
    shortdesc = models.TextField(db_column='shortDesc')  # Field name made lowercase.
    longdesc = models.TextField(db_column='longDesc', blank=True, null=True)  # Field name made lowercase.
    credits = models.CharField(max_length=255)
    runtime = models.IntegerField(blank=True, null=True)
    productionyear = models.CharField(db_column='productionYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    uploaded = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    moderated = models.DateTimeField(blank=True, null=True)
    moderatorid = models.IntegerField(db_column='moderatorID', blank=True, null=True)  # Field name made lowercase.
    moderatorcomments = models.TextField(db_column='moderatorComments', blank=True, null=True)  # Field name made lowercase.
    avgrating = models.IntegerField(db_column='avgRating', blank=True, null=True)  # Field name made lowercase.
    ratingcount = models.IntegerField(db_column='ratingCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movies1'


class Openmobile(models.Model):
    name = models.IntegerField()
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    eventname = models.IntegerField(db_column='eventName')  # Field name made lowercase.
    totalgrants = models.IntegerField(db_column='totalGrants')  # Field name made lowercase.
    grantdeadline = models.IntegerField(db_column='grantDeadline')  # Field name made lowercase.
    deadline = models.IntegerField(db_column='Deadline')  # Field name made lowercase.
    totalprizes = models.IntegerField(db_column='TotalPrizes')  # Field name made lowercase.
    tripbudget = models.IntegerField(db_column='TripBudget')  # Field name made lowercase.
    description = models.IntegerField()
    custom = models.IntegerField()
    downloadhash = models.IntegerField(db_column='downloadHash')  # Field name made lowercase.
    dlid = models.IntegerField(db_column='dlID')  # Field name made lowercase.
    name_exp_13 = models.IntegerField(db_column='Name_exp_13')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'openMobile'


class Openbriefs(models.Model):
    name = models.IntegerField()
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    eventname = models.IntegerField(db_column='eventName')  # Field name made lowercase.
    totalgrants = models.IntegerField(db_column='totalGrants')  # Field name made lowercase.
    grantdeadline = models.IntegerField(db_column='grantDeadline')  # Field name made lowercase.
    deadline = models.IntegerField(db_column='Deadline')  # Field name made lowercase.
    totalprizes = models.IntegerField(db_column='TotalPrizes')  # Field name made lowercase.
    tripbudget = models.IntegerField(db_column='TripBudget')  # Field name made lowercase.
    description = models.IntegerField()
    custom = models.IntegerField()
    downloadhash = models.IntegerField(db_column='downloadHash')  # Field name made lowercase.
    dlid = models.IntegerField(db_column='dlID')  # Field name made lowercase.
    name_exp_13 = models.IntegerField(db_column='Name_exp_13')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'openbriefs'


class OpenbriefsBack(models.Model):
    name = models.IntegerField()
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    eventname = models.IntegerField(db_column='eventName')  # Field name made lowercase.
    totalgrants = models.IntegerField(db_column='totalGrants')  # Field name made lowercase.
    grantdeadline = models.IntegerField(db_column='grantDeadline')  # Field name made lowercase.
    deadline = models.IntegerField(db_column='Deadline')  # Field name made lowercase.
    totalprizes = models.IntegerField(db_column='TotalPrizes')  # Field name made lowercase.
    tripbudget = models.IntegerField(db_column='TripBudget')  # Field name made lowercase.
    description = models.IntegerField()
    custom = models.IntegerField()
    downloadhash = models.IntegerField(db_column='downloadHash')  # Field name made lowercase.
    dlid = models.IntegerField(db_column='dlID')  # Field name made lowercase.
    name_exp_13 = models.IntegerField(db_column='Name_exp_13')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'openbriefs_back'


class Opensources(models.Model):
    name = models.IntegerField()
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    eventname = models.IntegerField(db_column='eventName')  # Field name made lowercase.
    totalgrants = models.IntegerField(db_column='totalGrants')  # Field name made lowercase.
    grantdeadline = models.IntegerField(db_column='grantDeadline')  # Field name made lowercase.
    deadline = models.IntegerField(db_column='Deadline')  # Field name made lowercase.
    totalprizes = models.IntegerField(db_column='TotalPrizes')  # Field name made lowercase.
    tripbudget = models.IntegerField(db_column='TripBudget')  # Field name made lowercase.
    description = models.IntegerField()
    custom = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'opensources'


class Originqueue(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    bulkid = models.IntegerField(db_column='bulkID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    queued = models.DateTimeField()
    profile = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=10)
    sent = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'originQueue'


class Originsourceprofile(models.Model):
    sourceid = models.IntegerField(db_column='sourceID', primary_key=True)  # Field name made lowercase.
    profile = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'originSourceProfile'


class Originxml(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    xml = models.TextField()
    received = models.DateTimeField()
    status = models.CharField(max_length=10)
    movieid = models.IntegerField(db_column='movieID', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'originXML'


class Paymentdetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hashkey = models.CharField(db_column='hashKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID', blank=True, null=True)  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID', blank=True, null=True)  # Field name made lowercase.
    grantid = models.IntegerField(db_column='grantID')  # Field name made lowercase.
    paymenttype = models.CharField(db_column='paymentType', max_length=14)  # Field name made lowercase.
    submitterid = models.IntegerField(db_column='submitterID', blank=True, null=True)  # Field name made lowercase.
    submittercomments = models.CharField(db_column='submitterComments', max_length=200, blank=True, null=True)  # Field name made lowercase.
    approverid = models.IntegerField(db_column='approverID', blank=True, null=True)  # Field name made lowercase.
    approvercomments = models.CharField(db_column='approverComments', max_length=300, blank=True, null=True)  # Field name made lowercase.
    payableamount = models.IntegerField(db_column='payableAmount')  # Field name made lowercase.
    paidamount = models.IntegerField(db_column='paidAmount', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=16)
    created = models.DateTimeField(blank=True, null=True)
    duedate = models.DateTimeField(db_column='dueDate', blank=True, null=True)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='paidDate', blank=True, null=True)  # Field name made lowercase.
    paymentdesc = models.CharField(db_column='PaymentDesc', max_length=300, blank=True, null=True)  # Field name made lowercase.
    accountuser = models.IntegerField(db_column='accountUser', blank=True, null=True)  # Field name made lowercase.
    accountcomments = models.CharField(db_column='accountComments', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bankreference = models.CharField(db_column='bankReference', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hasmultipart = models.IntegerField(db_column='hasMultipart', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymentDetails'


class Permissiongrouplinks(models.Model):
    permissionid = models.IntegerField(db_column='permissionID')  # Field name made lowercase.
    permissiongroupid = models.IntegerField(db_column='permissionGroupID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permissionGroupLinks'
        unique_together = (('permissionID', 'permissionGroupID'),)


class Permissiongroups(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'permissionGroups'


class Permissions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=60)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class PortalPortal(models.Model):
    brandid = models.IntegerField(db_column='brandID')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'portal_portal'


class PortalPortalcontent(models.Model):
    portalid = models.IntegerField(db_column='portalID')  # Field name made lowercase.
    contenttype = models.CharField(db_column='contentType', max_length=100)  # Field name made lowercase.
    licenseterms = models.TextField(db_column='licenseTerms')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    movies_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'portal_portalcontent'


class PortalPortalproject(models.Model):
    projectid = models.IntegerField(db_column='projectID')  # Field name made lowercase.
    name = models.CharField(max_length=100)
    portalid = models.IntegerField(db_column='portalID')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portal_portalproject'


class Productdata(models.Model):
    productid = models.IntegerField(db_column='productID')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productData'


class Products(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'products'


class Products1(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'products1'


class ProjectAssets(models.Model):
    name = models.CharField(max_length=32)
    projectid = models.IntegerField()
    type = models.CharField(max_length=32)
    path = models.CharField(max_length=128)
    hash = models.CharField(unique=True, max_length=32)
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_assets'


class Projects(models.Model):
    name = models.CharField(max_length=32)
    desc = models.TextField()
    brandid = models.IntegerField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    status = models.IntegerField()
    length = models.IntegerField()
    budget = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    hash = models.CharField(unique=True, max_length=32)
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'projects'


class Roles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'roles'


class Serviceactionlog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientID')  # Field name made lowercase.
    requesttime = models.DateTimeField(db_column='requestTime')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    actionname = models.CharField(db_column='actionName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serviceActionLog'


class Servicekey(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='clientName', max_length=100)  # Field name made lowercase.
    publickey = models.CharField(db_column='publicKey', max_length=200)  # Field name made lowercase.
    privatekey = models.CharField(db_column='privateKey', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serviceKey'


class Sourcebudget(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    grantbuffer = models.IntegerField(db_column='grantBuffer')  # Field name made lowercase.
    other = models.IntegerField()
    modifiedtime = models.DateTimeField(db_column='modifiedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sourceBudget'


class Sourcebudgetlog(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    srcid = models.IntegerField(db_column='srcID')  # Field name made lowercase.
    changelog = models.TextField(db_column='changeLog')  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='modifiedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sourceBudgetLog'


class Sourcedashboard(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.
    datatype = models.CharField(db_column='dataType', max_length=11)  # Field name made lowercase.
    productid = models.IntegerField(db_column='productID')  # Field name made lowercase.
    briefdownload = models.IntegerField(db_column='briefDownload', blank=True, null=True)  # Field name made lowercase.
    grantapplied = models.IntegerField(db_column='grantApplied', blank=True, null=True)  # Field name made lowercase.
    grantapproved = models.IntegerField(db_column='grantApproved', blank=True, null=True)  # Field name made lowercase.
    movieuploaded = models.IntegerField(db_column='movieUploaded', blank=True, null=True)  # Field name made lowercase.
    movieapproved = models.IntegerField(db_column='movieApproved', blank=True, null=True)  # Field name made lowercase.
    shortlisted = models.IntegerField(blank=True, null=True)
    winner = models.IntegerField(blank=True, null=True)
    ndadownload = models.IntegerField(db_column='ndaDownload', blank=True, null=True)  # Field name made lowercase.
    ndaapproved = models.IntegerField(db_column='ndaApproved', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='sortOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sourceDashboard'


class Sources(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.
    brandid = models.IntegerField(db_column='brandID')  # Field name made lowercase.
    name = models.CharField(max_length=40)
    webfilename = models.CharField(max_length=50, blank=True, null=True)
    hidden = models.CharField(max_length=1)
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    termsid = models.IntegerField(db_column='termsID', blank=True, null=True)  # Field name made lowercase.
    instructions = models.TextField(blank=True, null=True)
    bgcolor = models.CharField(max_length=10, blank=True, null=True)
    tripbudget = models.IntegerField()
    custom = models.CharField(max_length=1)
    status = models.CharField(max_length=11)
    sponsorid = models.IntegerField(db_column='sponsorID')  # Field name made lowercase.
    closedate = models.DateField(db_column='closeDate', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    rateid = models.IntegerField(db_column='rateID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sources'


class Sources1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.
    name = models.CharField(max_length=40)
    brandid = models.IntegerField(db_column='brandID')  # Field name made lowercase.
    webfilename = models.CharField(max_length=50, blank=True, null=True)
    hidden = models.CharField(max_length=1)
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    termsid = models.IntegerField(db_column='termsID', blank=True, null=True)  # Field name made lowercase.
    instructions = models.TextField(blank=True, null=True)
    bgcolor = models.CharField(max_length=10, blank=True, null=True)
    tripbudget = models.IntegerField()
    custom = models.CharField(max_length=1)
    status = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'sources1'


class Sourcesdata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.
    name = models.CharField(max_length=225)
    description = models.TextField()
    terms = models.TextField(blank=True, null=True)
    hash = models.CharField(max_length=32)
    lang = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'sourcesData'


class Sourcesprize(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.
    position = models.CharField(max_length=2)
    amount = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'sourcesPrize'


class Staticpages(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    controller = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    theme = models.CharField(max_length=25)
    metadescription = models.TextField(db_column='metaDescription')  # Field name made lowercase.
    metatags = models.TextField(db_column='metaTags')  # Field name made lowercase.
    lang = models.CharField(max_length=10)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staticpages'


class Suppliers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=80)
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'suppliers'


class SystemLogs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    application = models.CharField(max_length=100)
    process = models.CharField(max_length=100)
    message = models.TextField()
    criticality = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'system_logs'


class Tags(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=8)
    category = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class Teams(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'teams'


class Terms(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    replacesterms = models.IntegerField(db_column='replacesTerms', blank=True, null=True)  # Field name made lowercase.
    version = models.DateTimeField()
    description = models.TextField()
    htmllink = models.TextField(db_column='htmlLink', blank=True, null=True)  # Field name made lowercase.
    pdflink = models.TextField(db_column='pdfLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'terms'


class Territories(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    country = models.CharField(max_length=40)
    shortname = models.CharField(db_column='shortName', unique=True, max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'territories'


class Territorycurrencies(models.Model):
    territoryid = models.IntegerField(db_column='territoryID')  # Field name made lowercase.
    currencyid = models.IntegerField(db_column='currencyID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'territoryCurrencies'
        unique_together = (('territoryID', 'currencyID'),)


class Territorylanguages(models.Model):
    territoryid = models.IntegerField(db_column='territoryID')  # Field name made lowercase.
    languageid = models.IntegerField(db_column='languageID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'territoryLanguages'
        unique_together = (('territoryID', 'languageID'),)


class Territorystates(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    territoryid = models.IntegerField(db_column='territoryID')  # Field name made lowercase.
    description = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'territoryStates'


class Uploadqueue(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    bulkid = models.IntegerField(db_column='bulkID', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    queued = models.DateTimeField()
    profile = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=10)
    sent = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploadQueue'


class Uploadstatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    videocloudid = models.BigIntegerField(db_column='videoCloudID')  # Field name made lowercase.
    status = models.CharField(max_length=10)
    updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uploadStatus'


class Uploadedfiles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='sourceID')  # Field name made lowercase.
    uploadtype = models.CharField(db_column='uploadType', max_length=3)  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=255)  # Field name made lowercase.
    status = models.CharField(max_length=8)
    preferredlanguage = models.CharField(db_column='preferredLanguage', max_length=5)  # Field name made lowercase.
    created = models.DateTimeField()
    moderatorid = models.IntegerField(db_column='moderatorID', blank=True, null=True)  # Field name made lowercase.
    moderatorcomments = models.TextField(db_column='moderatorComments', blank=True, null=True)  # Field name made lowercase.
    moderated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploadedFiles'


class Useraffiliates(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    affiliate = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'userAffiliates'


class Useravatars(models.Model):
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    imagefilename = models.TextField(db_column='imageFilename')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userAvatars'


class Userdata(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    paramname = models.CharField(db_column='paramName', max_length=40)  # Field name made lowercase.
    paramvalue = models.TextField(db_column='paramValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userData'
        unique_together = (('userID', 'paramName'),)


class Userdownloads(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    downloadid = models.IntegerField(db_column='downloadID')  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ip = models.CharField(max_length=15)
    sourceid = models.IntegerField(db_column='sourceID', blank=True, null=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.
    country = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userDownloads'


class Usereventfavourites(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userEventFavourites'
        unique_together = (('userID', 'eventID'),)


class Usereventfilter(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    eventid = models.IntegerField(db_column='eventID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userEventFilter'
        unique_together = (('userID', 'eventID'),)


class Usereventpermissions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EventID')  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=50)  # Field name made lowercase.
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'userEventPermissions'


class Userfavourites(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userFavourites'
        unique_together = (('userID', 'movieID'),)


class Usergrantsattachment(models.Model):
    grantid = models.IntegerField(db_column='grantID')  # Field name made lowercase.
    path = models.TextField()
    hash = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'userGrantsAttachment'


class Userlicenses(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    trackid = models.IntegerField(db_column='trackID')  # Field name made lowercase.
    licenseid = models.CharField(db_column='licenseID', unique=True, max_length=255)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    trackname = models.TextField(db_column='trackName')  # Field name made lowercase.
    status = models.IntegerField()
    expirydate = models.DateTimeField(db_column='expiryDate')  # Field name made lowercase.
    musicsource = models.CharField(db_column='musicSource', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userLicenses'


class Userlog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    timestamp = models.DateTimeField()
    type = models.TextField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userLog'


class Userloginhashes(models.Model):
    hash = models.CharField(unique=True, max_length=255)
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    email = models.CharField(max_length=255)
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate')  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='expiryDate')  # Field name made lowercase.
    originatingipaddress = models.CharField(db_column='originatingIpAddress', max_length=50)  # Field name made lowercase.
    originatinguseragent = models.CharField(db_column='originatingUserAgent', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userLoginHashes'


class Usermoviegrants(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    grantid = models.IntegerField(db_column='grantID')  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID', blank=True, null=True)  # Field name made lowercase.
    filmconcept = models.TextField(db_column='filmConcept')  # Field name made lowercase.
    filmtitle = models.CharField(db_column='filmTitle', max_length=255)  # Field name made lowercase.
    duration = models.IntegerField(blank=True, null=True)
    usageofgrants = models.TextField(db_column='usageOfGrants')  # Field name made lowercase.
    requestedamount = models.FloatField(db_column='requestedAmount')  # Field name made lowercase.
    script = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    moderated = models.DateTimeField(blank=True, null=True)
    moderatorid = models.IntegerField(db_column='moderatorID', blank=True, null=True)  # Field name made lowercase.
    moderatorcomments = models.TextField(db_column='moderatorComments', blank=True, null=True)  # Field name made lowercase.
    messagestofilmmaker = models.TextField(db_column='messagesToFilmmaker', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=8, blank=True, null=True)
    grantedamount = models.FloatField(db_column='grantedAmount', blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(max_length=32)
    private = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userMovieGrants'


class Usermoviegrantsdata(models.Model):
    usermoviegrantsid = models.IntegerField(db_column='userMovieGrantsID')  # Field name made lowercase.
    paramname = models.CharField(db_column='paramName', max_length=40)  # Field name made lowercase.
    paramvalue = models.TextField(db_column='paramValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userMovieGrantsData'
        unique_together = (('userMovieGrantsID', 'paramName'),)


class Usermoviegrantsrating(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    grantid = models.IntegerField(db_column='grantID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userMovieGrantsRating'
        unique_together = (('grantID', 'userID'),)


class Userpermissions(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    permissionid = models.CharField(db_column='permissionID', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userPermissions'
        unique_together = (('userID', 'permissionID'),)


class Userpoints(models.Model):
    userid = models.IntegerField(db_column='userID', unique=True)  # Field name made lowercase.
    score = models.IntegerField()
    highscore = models.IntegerField(db_column='highScore')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userPoints'


class Userprivatemessagelog(models.Model):
    messageid = models.IntegerField(db_column='messageID', primary_key=True)  # Field name made lowercase.
    touserid = models.IntegerField(db_column='toUserID')  # Field name made lowercase.
    fromuserid = models.IntegerField(db_column='fromUserID')  # Field name made lowercase.
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=7)
    sentdate = models.DateTimeField(db_column='sentDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userPrivateMessageLog'


class Userprivatemessages(models.Model):
    messageid = models.AutoField(db_column='messageID', primary_key=True)  # Field name made lowercase.
    touserid = models.IntegerField(db_column='toUserID')  # Field name made lowercase.
    fromuserid = models.IntegerField(db_column='fromUserID')  # Field name made lowercase.
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=7)
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    readdate = models.DateTimeField(db_column='readDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userPrivateMessages'


class Userprofilemovies(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    movieid = models.IntegerField(db_column='movieID')  # Field name made lowercase.
    position = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.TextField()
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userProfileMovies'


class Userprofiles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    profilename = models.CharField(db_column='profileName', unique=True, max_length=50)  # Field name made lowercase.
    active = models.IntegerField()
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate')  # Field name made lowercase.
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userProfiles'


class Usersignupcodes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    territoryid = models.IntegerField(db_column='territoryID')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='startDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userSignupCodes'


class Usersourcepermissions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EventID')  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='SourceID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    hasevent = models.CharField(db_column='hasEvent', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userSourcePermissions'


class Userteams(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    teamid = models.IntegerField(db_column='teamID')  # Field name made lowercase.
    admin = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'userTeams'
        unique_together = (('userID', 'teamID'),)


class Userterms(models.Model):
    userid = models.IntegerField(db_column='userID')  # Field name made lowercase.
    termsid = models.IntegerField(db_column='termsID')  # Field name made lowercase.
    version = models.DateTimeField()
    agreed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'userTerms'
        unique_together = (('userID', 'termsID'),)


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=70)
    enabled = models.CharField(max_length=1)
    territoryid = models.IntegerField(db_column='territoryID', blank=True, null=True)  # Field name made lowercase.
    facebookid = models.BigIntegerField(db_column='facebookID', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    registered = models.DateTimeField()
    regip = models.CharField(db_column='regIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(unique=True, max_length=32, blank=True, null=True)
    autocommitstatus = models.IntegerField(db_column='autoCommitStatus', blank=True, null=True)  # Field name made lowercase.
    userrole = models.IntegerField(db_column='userRole')  # Field name made lowercase.
    proenabled = models.IntegerField(db_column='proEnabled')  # Field name made lowercase.
    proonly = models.IntegerField(db_column='proOnly')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
