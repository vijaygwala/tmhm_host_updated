from django.contrib import admin

# By vijay
admin.AdminSite.site_title = "TMHM PVT LTD"
#admin.AdminSite.index_title = ""
admin.AdminSite.site_header = "TMHM PVT LTD "
admin.AdminSite.login_template='admin_login.html'
#endVijay

# Register your models here.
from .models import Signup , OnlineCounselling
admin.site.register(Signup)
admin.site.register(OnlineCounselling)