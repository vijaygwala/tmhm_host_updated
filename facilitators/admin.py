


from django.contrib import admin

from .models import *


    
class ExperienceAdmin(admin.ModelAdmin):
    list_display=('Eid','Linkedin_Url','Website_Url','Youtube_Url','RExperience','TExperience','facilitator')
class FacilitatorQueriesAdmin(admin.ModelAdmin):
    ist_display=('Qid','query','status','user')

admin.site.register(FacilitatorQueries,FacilitatorQueriesAdmin)
admin.site.register(Experience,ExperienceAdmin)
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)