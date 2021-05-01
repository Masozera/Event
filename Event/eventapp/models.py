from django.db import models

# Create your models here.

class Speaker(models.Model):
    name            = models.CharField(max_length=100, blank=True)
    pic             = models.ImageField(upload_to='speaker_pics')
    title           = models. CharField(max_length=100, blank=True)
    facebook_link   = models.CharField(max_length = 100, blank=True)
    twitter_link     = models.CharField(max_length = 100, blank=True)

    def __str__(self):
        return self.name



class Participant (models.Model):
    STATUS = (
        ('Inperson', 'Inperson'),
        ('Virtually', 'Virtually'),
    )
    name           = models.CharField(max_length=100, blank=True)
    email          = models.CharField(max_length = 100, blank = True)
    Attendance     = models.CharField(max_length = 100, blank = True)
    Nationality    = models.CharField(max_length = 100, blank = True)
    Phone_number   = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    name   = models.CharField(max_length=100, blank=True)
    email  = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Newslettersubcriber(models.Model):
    email   =  models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.email

class  Sociallink(models.Model):
    facebook = models.CharField(max_length = 100, blank = True)
    twitter  = models.CharField(max_length = 100, blank = True)
    linkedin = models.CharField(max_length= 100, blank = True)




