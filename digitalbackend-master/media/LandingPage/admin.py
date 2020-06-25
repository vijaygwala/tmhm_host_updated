from django.contrib import admin

# Register your models here.
from .models import Signup , OnlineCounselling
admin.site.register(Signup)
admin.site.register(OnlineCounselling)