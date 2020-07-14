from django.db import models
from myauth.models import *
# Create your models here.
from django.db.models.signals import post_delete
#from django.dispatch import receive


#this table contain all the categories
class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.name

#this relation contains all the subcategories releted to particuler categories
class SubCategory(models.Model):
    subCat_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#this relation contains all the courses releted to particuler subcategory
class Course(models.Model):
    Cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False,blank=False)
    title=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(blank=False,null=True)
    subCat_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#this relation associate a particuler facilitator with particuler course
class offer(models.Model):
    Fid = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# class contact(models.Model):
#     msg_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50,default='')
#     email = models.CharField(max_length=30,default='')
#     msg = models.CharField(max_length=1000,default='')'''

# class Signup(models.Model):
#     Signup_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=60,default='')
#     email = models.CharField(max_length=50,default='')
#     phone= models.CharField(max_length=20,default='')
#     city= models.CharField(max_length=100,default='')
#     Poi=models.CharField(max_length=100,default='')

#     def __str__(self):
#         return self.email

# class OnlineCounselling(models.Model):
#     OC_id = models.AutoField(primary_key=True)
#     phone = models.CharField(max_length=20,default='')

# '''#Delete attached file when we delete a instance of object
# @receiver(post_delete, sender=Signup)
# def submission_delete(sender, instance, **kwargs):
#     instance.file.delete(False)'''