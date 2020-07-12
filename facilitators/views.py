from django.shortcuts import render , redirect
from facilitators.models import *
from facilitators.forms import *
from django.contrib.auth import authenticate,login
from django.views import View
import random
import string
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# # # Create your views here.
# # def home(request):
# #     if request.method=='POST':
# #         tname=request.POST.get('tname','')
# #         temail=request.POST.get('temail','')
# #         texp1=request.POST.get('texp1','')
# #         texp2=request.POST.get('texp2','')
# #         tphone=request.POST.get('tphone','')
# #         turl=request.POST.get('turl','')
# #         #tprofile=request.POST.get('tprofile','')
# #         q_s=request.POST.get('q/s','')
# #         tprofile=request.FILES['tprofile']
# #         trainer = Trainer(tname=tname,q_s=q_s,temail=temail,tphone=tphone,texp1=texp1,texp2=texp2,turl=turl,tprofile=tprofile)
# #         trainer.save()
# #     return render(request,'facilitators/index.html')


# # def facilitatorRegistration(request):
# #     print("entering function")
# #     if request.method=='POST':
# #         # fname=request.POST.get('fname','')
# #         # lname=request.POST.get('lname','')
# #         # name=fname+" "+lname 
# #         # phone=request.POST.get('phone','')
# #         # link1=request.POST.get('linkedin','')
# #         # link2=request.POST.get('website','')
# #         # link3=request.POST.get('youtube','')
# #         # password1=request.POST.get('password1','')
# #         # password2=request.POST.get('password2','')
# #         # email=request.POST.get('email','')
# #         # releventExp=request.POST.get('rexp','')
# #         # totalExp=request.POST.get('texp','')
# #         # #subCat=request.POST.get('subCat','')
# #         # #portfolio=request.FILES['portfolio']
# #         print("before saving")
# #         facilitator = FacilitatorForm(request.post)
# #         # experience=  Experience(Linkedin_Url=link1,Website_Url=link2,Youtube_Url=link3,RExperience=releventExp,TExperience=releventExp)
# #         # userinfo=FacilitatorRegistrationForm(first_name=fname,last_name=lname,email=email)
# #         facilitator.save()
# #         experience.save()
# #         userinfo.save()
# #     return render(request,'facilitators/index.html')


def facilitator_page(request):
    return render(request, 'facilitators/index.html')

# # def FacilitatorAuthentication(self,request):
# #     context={}
# #     username=self.cleaned_data.get('username')
# #     password=self.cleaned_data.get('password1')
# #     user=authenticate(username=username , password=password)
# #     if user is not None:
# #         if user.is_active:
# #             login(request, user)
# #             return render(request, 'facilitators/index.html')

                
# #         else:
# #             context['error_message'] = "user is not active"
# #             print(context['error_message'])
# #     else:
# #         context['error_message'] = "email or password not correct"
# #         print(context['error_message'])
# #     return render(request,'facilitators/register/index.html', context)

# #  facilitatorForm = FacilitatorForm(request.POST)
# #         userForm=FacilitatorRegistrationForm(request.POST)
# #         #print("yha tk")
# #         print(facilitatorForm)
# #         print(userForm)
# #         if userForm.is_valid() and facilitatorForm.is_valid():
# #             user=userForm.save()
# #             facilitator=facilitatorForm.save(commit=False)
# #             facilitator.user=user
# #             facilitator.save()
# #             email=userForm.cleaned_data.get('email')
           
# #             try:   
# #                 username = User.objects.get(email=email.lower()).username
# #             except username.DoesNotExist:
# #                 return None
# #             password=userForm.cleaned_data.get('password1')
# #             user=authenticate(username=username , password=password)
# #             if user is not None:
# #                 if user.is_active:
# #                     login(request, user)
# #                     return render(request, 'facilitators/index.html')

                
# #                 else:
# #                     context['error_message'] = "user is not active"
# #             else:
# #                 context['error_message'] = "email or password not correct"
# #             return render(request, self.template_name, context)



    
from django.views.generic import CreateView
from .mixins import AjaxFormMixin
def signup(request):
    context = {'form': UserForm(),'expform':ExperienceForm(),'fquery':FacilitatorQueriesForm()}
    return render(request, 'facilitators/register/mysignup.html',context)


class RegisterLoginView(AjaxFormMixin,View):
    def get(self, request, *args, **kwargs):
        context = {'form': UserForm(),'expform':ExperienceForm(),'fquery':FacilitatorQueriesForm()}
        return render(request, 'facilitators/register/mysignup.html', context)

    def post(self, request, *args, **kwargs):
        context = {'form': UserForm(),'expform':ExperienceForm(),'fquery':FacilitatorQueriesForm()}
        form = UserForm(request.POST)
        expform = ExperienceForm(request.POST)
        phone=request.POST.get('phone','')
        portfolio = request.FILES['pro']
        fquery=FacilitatorQueriesForm(request.POST)
        course=request.POST.getlist('course','')
        catlist=""
        for cat in course:
            catlist+=cat+","
        print(course)
        user=None
        try:
            if form.is_valid():
                user=form.save()
                profile=Profile.objects.get(user=user.id)
                profile.phone=phone
                profile.portfolio=portfolio
                profile.role=2
                profile.intrest=catlist
                profile.save()
            else:
                raise form.ValidationError("something went wrong !")
        except:
            messages.error(request, ('Something went Wrong !'))
            return redirect('facilitator-register')
            
       
        try:
            if expform.is_valid():
                ex=expform.save(commit=False)
                ex.facilitator=user
                ex.save()
            else:
                raise expform.ValidationError("something went wrong !")
        except:
            messages.error(request, ('Something went Wrong !'))
            return redirect('facilitator-register')

        if fquery!=None:
            try:
                if fquery.is_valid():
                    qo=fquery.save(commit=False)
                    qo.user=user
                    qo.save()
                else:
                    raise fquery.ValidationError("something went wrong !")
            except:
                messages.error(request, ('Something went Wrong !'))
                return redirect('facilitator-register')
       

        messages.success(request, ('Your profile was successfully Created!'))
        return redirect('facilitator-register')