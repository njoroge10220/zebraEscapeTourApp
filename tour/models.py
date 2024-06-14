from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    package = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='Place_image')
    url = models.URLField(blank=True)
    day = models.IntegerField(null=True)
    offer = models.CharField(max_length=255, null=True)
               
    
    def __str__(self):
        return self.name


class Picture(models.Model):
    place = models.ForeignKey(Place, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='viewImages')
    
    def __str__(self):
        return self.place.name


class Place_Wording(models.Model):
    place = models.ForeignKey(Place, default=None, on_delete=models.CASCADE)
    overview = models.TextField(blank=True, null=True)
    pricing = models.IntegerField()
    reviews = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.place.name
    

class Listing(models.Model):
    List_Name = models.CharField(max_length=100)
    No_Listing = models.IntegerField()
    url = models.URLField(blank=True)    
    
    def __str__(self):
        return self.List_Name      
        
    
class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.IntegerField()
    instagram =  models.URLField(blank=True)
    facebook =  models.URLField(blank=True)
    whatsApp =  models.URLField(blank=True)      
    
    def __str__(self):
        return self.email
    
    
class Website_Image(models.Model):
    email = models.ForeignKey(Contact, default=None, on_delete=models.CASCADE)
    Icon = models.ImageField(upload_to='webImages', default=None, null=True)
    Log = models.ImageField(upload_to='webImages', default=None, null=True)
    Name = models.ImageField(upload_to='webImages', default=None, null=True)
    
    def __str__(self):
        return self.email.email
    

class Regular_User (AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    con_password = models.CharField(max_length=100)
    
    is_logged_in = models.BooleanField(default=False)
    last_login = models.DateTimeField(('last login'), blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.username}-{self.email}-{self.password}-{self.con_password}-{self.is_logged_in}-{self.last_login}"
    

class Feedback(models.Model):
    user = models.ForeignKey(Regular_User, default=None, on_delete=models.CASCADE)
    feedback = models.TextField()
    creat_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

    