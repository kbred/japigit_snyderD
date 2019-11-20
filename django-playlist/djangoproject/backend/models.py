from django.db import models

class TransferredSubscription(models.Model):
    transferfrom = models.CharField(max_length=50)
    transferto = models.CharField(max_length=50)
    requestdate = models.DateTimeField()
    transferdate = models.DateTimeField()
    subscriberID = models.ForeignKey('Subscriber', on_delete=models.CASCADE)

class Subscriber(models.Model):
    username = models.CharField(max_length=50)
    subscriptiontypecode = models.CharField(max_length=50)
    servicecode = models.CharField(max_length=50)
    requestdate = models.DateTimeField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    motifofcancellation = models.TextField()

    def __str__(self):
        return self.username

class Officer(models.Model):
    officecode = models.ForeignKey('Office', on_delete=models.CASCADE)
    subscriberID = models.ForeignKey('Subscriber', on_delete=models.CASCADE)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()

class OrganizationMember(models.Model):
    organizationcode = models.ForeignKey('Organization', on_delete=models.CASCADE)
    subscriberID = models.ForeignKey('Subscriber', on_delete=models.CASCADE)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    nativecountry = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=20)
    isdelegate = models.CharField(max_length=20)

class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(null=True)
    employername = models.CharField(max_length=20)

class SubscriptionType(models.Model):
    subscriptiontypecode = models.IntegerField()
    subscriptiontypename = models.CharField(max_length=50)

class Service(models.Model):
    servicecode = models.IntegerField()
    servicename = models.CharField(max_length=20)
    description = models.TextField()
    premium = models.BooleanField()
    allocation = models.CharField(max_length=50)

class Office(models.Model):
    officecode = models.IntegerField()
    officename = models.CharField(max_length=50)
    attribution = models.TextField()

class Organization(models.Model):
    organizationcode = models.IntegerField()
    organizationname = models.CharField(max_length=50)
    description = models.TextField()
    datejoined = models.DateTimeField()
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(null=True)
    phonenumber = models.IntegerField(null=True)
