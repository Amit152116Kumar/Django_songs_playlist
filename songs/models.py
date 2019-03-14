from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    Username = models.OneToOneField(User,on_delete=models.CASCADE)
    Image    = models.ImageField(null=True,default='default/profile.png')

    def __str__(self):
        return str(self.Username)
    class Meta :
        ordering =['Username']


class Song(models.Model):
    owner       = models.ForeignKey(Profile ,on_delete=models.CASCADE)
    Title       = models.CharField(max_length=30)
    Album       = models.ForeignKey('Album',on_delete=models.CASCADE,null=True,blank= True)
    Artist      = models.ManyToManyField('Artist', blank=True)
    Lyrics      = models.TextField(null=True,blank=True)
    Duration    = models.DurationField(null=True,blank= True,help_text='Please use the following '
                                                                       'format: <em>hh-mm-ss</em>')


    def __str__(self):
        return self.Title

    class Meta :
        ordering =['Title']


class Album(models.Model):
    owner       = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Title       = models.CharField(max_length=30,unique=True)
    Released_on = models.DateField(null=True, blank=True,help_text='Format : YYYY-MM-DD')
    Cover       = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.Title

    class Meta :
        ordering =['Title']


class Artist(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Title    = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.Title

    class Meta :
        ordering =['Title']
