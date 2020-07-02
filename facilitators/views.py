from django.shortcuts import render
from facilitators.models import *
from facilitators.forms import *

# # Create your views here.
# def home(request):
#     if request.method=='POST':
#         tname=request.POST.get('tname','')
#         temail=request.POST.get('temail','')
#         texp1=request.POST.get('texp1','')
#         texp2=request.POST.get('texp2','')
#         tphone=request.POST.get('tphone','')
#         turl=request.POST.get('turl','')
#         #tprofile=request.POST.get('tprofile','')
#         q_s=request.POST.get('q/s','')
#         tprofile=request.FILES['tprofile']
#         trainer = Trainer(tname=tname,q_s=q_s,temail=temail,tphone=tphone,texp1=texp1,texp2=texp2,turl=turl,tprofile=tprofile)
#         trainer.save()
#     return render(request,'facilitators/index.html')


# def facilitatorRegistration(request):
#     print("entering function")
#     if request.method=='POST':
#         # fname=request.POST.get('fname','')
#         # lname=request.POST.get('lname','')
#         # name=fname+" "+lname 
#         # phone=request.POST.get('phone','')
#         # link1=request.POST.get('linkedin','')
#         # link2=request.POST.get('website','')
#         # link3=request.POST.get('youtube','')
#         # password1=request.POST.get('password1','')
#         # password2=request.POST.get('password2','')
#         # email=request.POST.get('email','')
#         # releventExp=request.POST.get('rexp','')
#         # totalExp=request.POST.get('texp','')
#         # #subCat=request.POST.get('subCat','')
#         # #portfolio=request.FILES['portfolio']
#         print("before saving")
#         facilitator = FacilitatorForm(request.post)
#         # experience=  Experience(Linkedin_Url=link1,Website_Url=link2,Youtube_Url=link3,RExperience=releventExp,TExperience=releventExp)
#         # userinfo=FacilitatorRegistrationForm(first_name=fname,last_name=lname,email=email)
#         facilitator.save()
#         experience.save()
#         userinfo.save()
#     return render(request,'facilitators/index.html')


def facilitator_page(request):
    return render(request, 'facilitators/index.html')


def register(request):
    context={}
    if request.method=='POST':
        
        facilitator = FacilitatorForm(request.POST)
        print("yha tk")
        print(facilitator)
        if facilitator.is_valid():
            facilitator.save()
            print("save succesfully")
    else:
        print("before saving")
        facilitator = FacilitatorForm()
        context={"form":facilitator}


    return render(request, 'facilitators/register/index.html',context)