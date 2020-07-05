# from django.contrib import admin
# from .models import  (Facilitator,Category,Course,offer,Experience,SubCategory,FacilitatorQueries,FacilitatorQueriesAnswer)
# class FacilitatorAdmin(admin.ModelAdmin):
#     list_display=('Fid','name','DOB','phone','PAddress','TAddress','profile','user')
# class ExperienceAdmin(admin.ModelAdmin):
#     list_display=('Eid','Linkedin_Url','Website_Url','Youtube_Url','RExperience','TExperience','facilitator')
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=('cat_id','name')
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display=('subCat_id','name','cat_id')
# class CourseAdmin(admin.ModelAdmin):
#     list_display=('Cid','name','title','description','subCat_id')
# class offerAdmin(admin.ModelAdmin):
#     list_display=('Fid','Cid')
# class FacilitatorQueriesAdmin(admin.ModelAdmin):
#     list_display=('Qid','query','status','Fid')
# class FacilitatorsQueriesAnswerAdmin(admin.ModelAdmin):
#     list_display=('Aid','Answer','status','Qid')




# admin.site.register(Facilitator,FacilitatorAdmin)
# admin.site.register(Experience,ExperienceAdmin)
# admin.site.register(Category,CategoryAdmin)
# admin.site.register(SubCategory,SubCategoryAdmin)
# admin.site.register(Course,CourseAdmin)
# admin.site.register(offer,offerAdmin)
# admin.site.register(FacilitatorQueries,FacilitatorQueriesAdmin)
# admin.site.register(FacilitatorQueriesAnswer,FacilitatorsQueriesAnswerAdmin)



# #admin.site.register(Trainer)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_Address')
    list_select_related = ('profile', )

    def get_Address(self, instance):
        return instance.profile.Address
    get_Address.short_description = 'Location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class ExperienceAdmin(admin.ModelAdmin):
    list_display=('Eid','Linkedin_Url','Website_Url','Youtube_Url','RExperience','TExperience','facilitator')
class FacilitatorQueriesAdmin(admin.ModelAdmin):
    ist_display=('Qid','query','status','user')

admin.site.register(FacilitatorQueries,FacilitatorQueriesAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)