from django.db import models

# Create your models here.
from django.db.models.signals import post_delete
from django.dispatch import receiver
'''

class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=30,default='')
    msg = models.CharField(max_length=1000,default='')'''

class Signup(models.Model):
    Signup_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60,default='')
    email = models.CharField(max_length=50,default='')
    phone= models.CharField(max_length=20,default='')
    city= models.CharField(max_length=100,default='')
    Poi=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.email

class OnlineCounselling(models.Model):
    OC_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20,default='')

'''#Delete attached file when we delete a instance of object
@receiver(post_delete, sender=Signup)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False)'''