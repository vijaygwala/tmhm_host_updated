from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    #path('facilitator/', views.facilitator_page),
    path('facilitator/$', views.facilitator_page,name='facilitator'),
    path('facilitator-register/', views.register,name='facilitator-register')

]
