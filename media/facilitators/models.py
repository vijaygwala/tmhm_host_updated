from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.
class Trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=50,default='')
    temail = models.CharField(max_length=30,default='')
    tphone = models.CharField(max_length=10,default='')
    texp1 = models.CharField(max_length=30,default='')
    texp2 = models.CharField(max_length=30,default='')
    turl = models.CharField(max_length=30,default='')
    q_s = models.CharField(max_length=500,default='')
    tprofile = models.FileField(upload_to='facilitators/profile')

#Delete attached file when we delete a instance of object
@receiver(post_delete, sender=Trainer)
def submission_delete(sender, instance, **kwargs):
    instance.tprofile.delete(False)