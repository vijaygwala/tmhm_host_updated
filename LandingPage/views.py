from django.shortcuts import render
from .models import Signup,OnlineCounselling
# Create your views here.
def home(request):
    return render(request,'LandingPage/index.html')


def home_page(request):
    pass
    '''if request.method=='POST':
        if request.POST.get("f_name"):
            f_name=request.POST.get('f_name','')
            l_name=request.POST.get('l_name','')
            city=request.POST.get('city','')
            email=request.POST.get('email','')
            phone=request.POST.get('phone','')
            poi=request.POST.get('poi','')
            name = f_name+' '+l_name
            signup = Signup(name=name,city=city,email=email,phone=phone,Poi=poi)
            signup.save()
        if request.POST.get('ocphone'):
            phone = request.POST.get('ocphone','')
            councelling = OnlineCounselling(phone=phone)
            councelling.save()
    return render(request, 'LandingPage/index.html')'''