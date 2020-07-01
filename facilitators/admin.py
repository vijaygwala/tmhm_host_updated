from django.contrib import admin
from .models import  (Facilitator,Category,Course,offer,Experience,SubCategory,FacilitatorQueries,FacilitatorQueriesAnswer)
class FacilitatorAdmin(admin.ModelAdmin):
    list_display=('Fid','name','DOB','phone','PAddress','TAddress','profile','Uid')
class ExperienceAdmin(admin.ModelAdmin):
    list_display=('Eid','Linkedin_Url','Website_Url','Youtube_Url','RExperience','TExperience','Fid')
class CategoryAdmin(admin.ModelAdmin):
    list_display=('cat_id','name')
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=('subCat_id','name','cat_id')
class CourseAdmin(admin.ModelAdmin):
    list_display=('Cid','name','title','description','subCat_id')
class offerAdmin(admin.ModelAdmin):
    list_display=('Fid','Cid')
class FacilitatorQueriesAdmin(admin.ModelAdmin):
    list_display=('Qid','query','status','Fid')
class FacilitatorsQueriesAnswerAdmin(admin.ModelAdmin):
    list_display=('Aid','Answer','status','Qid')




admin.site.register(Facilitator,FacilitatorAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(offer,offerAdmin)
admin.site.register(FacilitatorQueries,FacilitatorQueriesAdmin)
admin.site.register(FacilitatorQueriesAnswer,FacilitatorsQueriesAnswerAdmin)



#admin.site.register(Trainer)