from django.shortcuts import render
from facilitators.models import *
from facilitators.forms import *
from django.contrib.auth import authenticate,login
from django.views import View
import random
import string

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

# def FacilitatorAuthentication(self,request):
#     context={}
#     username=self.cleaned_data.get('username')
#     password=self.cleaned_data.get('password1')
#     user=authenticate(username=username , password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             return render(request, 'facilitators/index.html')

                
#         else:
#             context['error_message'] = "user is not active"
#             print(context['error_message'])
#     else:
#         context['error_message'] = "email or password not correct"
#         print(context['error_message'])
#     return render(request,'facilitators/register/index.html', context)

#  facilitatorForm = FacilitatorForm(request.POST)
#         userForm=FacilitatorRegistrationForm(request.POST)
#         #print("yha tk")
#         print(facilitatorForm)
#         print(userForm)
#         if userForm.is_valid() and facilitatorForm.is_valid():
#             user=userForm.save()
#             facilitator=facilitatorForm.save(commit=False)
#             facilitator.user=user
#             facilitator.save()
#             email=userForm.cleaned_data.get('email')
           
#             try:   
#                 username = User.objects.get(email=email.lower()).username
#             except username.DoesNotExist:
#                 return None
#             password=userForm.cleaned_data.get('password1')
#             user=authenticate(username=username , password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return render(request, 'facilitators/index.html')

                
#                 else:
#                     context['error_message'] = "user is not active"
#             else:
#                 context['error_message'] = "email or password not correct"
#             return render(request, self.template_name, context)


# def register(request):
#     context={}
#     if request.method=='POST':
       
class RegisterLoginView(View):
    template_name = 'facilitators/register/index.html'
    context={}
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        
        data = request.POST.copy()
        data['name'] = data['first_name']+" "+data['last_name']
                                   
        facilitatorForm = FacilitatorForm(data)
        userForm=FacilitatorRegistrationForm(request.POST)
        
        
        experienceForm=ExperienceForm(data)
    
        user=None
        qo=None
        exp=None
        facilitator=None
        if userForm.is_valid():  
            user=userForm.save()
        else:
            print("invalid user form")
        if facilitatorForm.is_valid():
        
            facilitator=facilitatorForm.save(commit=False)
            facilitator.user=user
            facilitator.save()
        else:
            print("invalid facilitator form")
       
        if experienceForm.is_valid():      
            exp=experienceForm.save(commit=False)
            exp.facilitator=facilitator
            exp.save()
        else :
            print("invalid experience form")
        query=data.POST.get('query',None)
        
        if query!=None:
            qo=FacilitatorQueries(query=query,Fid=facilitator)
            qo.save()
            
        else :
            print("there is no  query")
        
        #FacilitatorAuthentication(userForm,request)

        

        return render(request, self.template_name,context)

            
    