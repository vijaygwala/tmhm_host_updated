from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    LEARNER = 1
    FACILITATOR = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (LEARNER, 'Learner'),
        (FACILITATOR, 'Facilitator'),
        (ADMIN, 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Address = models.CharField(max_length=30, blank=True)
    DOB = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    phone=models.CharField(max_length=13,blank=False)
    portfolio = models.FileField(upload_to ='uploads/% Y/% m/% d/')
    profile=models.ImageField(upload_to ='Mentor_profiles/% Y/% m/% d/',default='default.png')
    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()










# #this relation contains all the facilitators
# class Facilitator(models.Model):
#     Fid=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=100,null=True,blank=True)
#     DOB=models.DateField(blank=True,null=True)
#     phone=models.CharField(max_length=13,blank=False)
#     PAddress=models.TextField(blank=True,null=True)
#     TAddress=models.TextField(blank=True,null=True)
#     portfolio = models.FileField(upload_to ='uploads/% Y/% m/% d/')
#     profile=models.ImageField(upload_to ='Mentor_profiles/% Y/% m/% d/',default='default.png')
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name


# #this relation contain experience info refers to the particuler Facilitator
class Experience(models.Model):
    Eid=models.AutoField(primary_key=True)
    Linkedin_Url= models.URLField(max_length=250)
    Website_Url= models.URLField(max_length=250)
    Youtube_Url= models.URLField(max_length=250)
    RExperience=models.TextField()
    TExperience=models.TextField()
    facilitator= models.OneToOneField(User, on_delete=models.CASCADE)

# #this table contain all the categories
# class Category(models.Model):
#     cat_id=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=100,null=False,blank=False)
#     def __str__(self):
#         return self.name

# #this relation contains all the subcategories releted to particuler categories
# class SubCategory(models.Model):
#     subCat_id=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=100,null=False,blank=False)
#     cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name

# #this relation contains all the courses releted to particuler subcategory
# class Course(models.Model):
#     Cid=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=100,null=False,blank=False)
#     title=models.CharField(max_length=100,null=False,blank=False)
#     description=models.TextField(blank=False,null=True)
#     subCat_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name

# #this relation associate a particuler facilitator with particuler course
# class offer(models.Model):
#     Fid = models.ForeignKey(Facilitator, on_delete=models.CASCADE)
#     Cid = models.ForeignKey(Course, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name

# #this realtion contains all the quries to the particuler facilitator
class FacilitatorQueries(models.Model):
    STATUS=(('R','Resolved'),('D','Doubt'))
    Qid=models.AutoField(primary_key=True)
    query=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=1,choices=STATUS,null=False,default="Doubt")
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.query

# #this relation contains all the answer releted to particuler question
# class FacilitatorQueriesAnswer(models.Model):
#     STATUS=(('R','Resolved'),('D','Doubt'))
#     Aid=models.AutoField(primary_key=True)
#     Answer=models.TextField(blank=True,null=True)
#     status=models.CharField(max_length=1,choices=STATUS,null=False,default=None)
#     Qid = models.ForeignKey(FacilitatorQueries, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.Answer






