from django.shortcuts import render
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


# # def register(request):
# #     context={}
# #     if request.method=='POST':
       
# # class RegisterLoginView(View):
# #     template_name = 'facilitators/register/index.html'
# #     context={}
# #     def get(self, request):
# #         facilitatorForm = FacilitatorForm()
# #         userForm=FacilitatorRegistrationForm()
# #         experienceForm=ExperienceForm()
# #         context={
# #             'facilitatorForm':facilitatorForm,
# #             'userForm':userForm,
# #             'experienceForm': experienceForm
# #         }

# #         return render(request, self.template_name,context)

# #     def post(self, request):
        
# #         data = request.POST.copy()
# #         data['name'] = data['first_name']+" "+data['last_name']
                                   
# #         facilitatorForm = FacilitatorForm(data)
# #         userForm=FacilitatorRegistrationForm(request.POST)

        
# #         experienceForm=ExperienceForm(data)
    
# #         user=None
# #         qo=None
# #         exp=None
# #         facilitator=None
# #         if userForm.is_valid():  
# #             user=userForm.save()
# #         else:
# #             print("invalid user form")
# #         if facilitatorForm.is_valid():
        
# #             facilitator=facilitatorForm.save(commit=False)
# #             facilitator.user=user
# #             facilitator.save()
# #         else:
# #             print("invalid facilitator form")
       
# #         if experienceForm.is_valid():      
# #             exp=experienceForm.save(commit=False)
# #             exp.facilitator=facilitator
# #             exp.save()
# #         else :
# #             print("invalid experience form")
# #         query=data.POST.get('query',None)
        
# #         if query!=None:
# #             qo=FacilitatorQueries(query=query,Fid=facilitator)
# #             qo.save()
            
# #         else :
# #             print("there is no  query")
        
# #         #FacilitatorAuthentication(userForm,request)

        

# #         return render(request, self.template_name,context)

# class RegisterLoginView(View):
#     template_name = 'facilitators/register/index.html'
    
#     def get(self, request):
#         context={}
#         form=UserCreationForm()
#         return render(request, self.template_name,context={'form':form})

#     def post(self,request):
#         context={}
#         fname = request.POST.get("first_name")
#         lname = request.POST.get("last_name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         password = request.POST.get("password1")
#         confirm_password = request.POST.get("password2")
#         portfolio = request.POST.get("portfolio")
#         linkedinprofile = request.POST.get("Linkedin_Url")
#         blogurl = request.POST.get("Website_Url")
#         youtubechannel = request.POST.get("Youtube_Url")
#         rexp = request.POST.get("RExperience")
#         texp=request.POST.get("TExperience")
#         query=request.POST.get("query",None)
#         if password != confirm_password:
#             messages.error(request, "confirm passowrd not matches with password entered")
#             return HttpResponseRedirect("/facilitator-register")

        
#         form=UserCreationForm(request.POST)
#         try:
#             if form.is_valid():
#                 form.save()
#                 username = form.cleaned_data.get('username')
#                 raw_password = form.cleaned_data.get('password1')
#                 user = authenticate(username=username, password=raw_password)
#                 login(request, user)
#         except:
#             messages.error(request, "something went wrong with userform regirstration")

#         try:
#             facilitator=Facilitator(name=fname+lname,phone=phone,portfolio=portfolio,user=request.user)
#             facilitator.save()
#         except:
#             messages.error(request, "something went wrong with facilitator regirstration")
#         try:
#             exp=Experience(Linkedin_Url=linkedinprofile, Website_Url=blogurl,Youtube_Url=youtubechannel,RExperience=rexp,TExperience=texp,facilitator=facilitator)
#             exp.save()
#         except:
#             messages.error(request,"something went wrong with experience regirstration")
#         try:
#             if query!=None:
#                 qo=FacilitatorQueries(query=query,Fid=facilitator.Fid)
#                 qo.save()
#         except:
#             messages.error(request,"something went wrong with query regirstration")
        
#         return render(request,'facilitators/index.html', context)

# class RegisterLoginView(View):
#     template_name = 'facilitators/register/index.html'
    
#     def get(self, request):
    
#         user_form = UserForm()
#         profile_form = ProfileForm()
#         return render(request, self.template_name,context={'form':user_form,'profile_form':profile_form})

#     def post(self,request):
#         if request.method == 'POST':
#             user_form = UserForm(request.POST)
#             profile_form = ProfileForm(request.POST)
#             if user_form.is_valid() :#and profile_form.is_valid():
#                 user_form.save()
#                 #profile_form.save()
#                 messages.success(request, ('Your profile was successfully updated!'))
#                 return HttpResponseRedirect('facilitators/index.html')
#             else:
#                 messages.error(request, ('Please correct the error below.'))
     
#             return render(request, 'facilitators/index.html')   

    
from django.views.generic import CreateView

class RegisterLoginView(CreateView):
    def get(self, request, *args, **kwargs):
        personal_detail={'first_name':'First name','last_name':'Last name','username':'Username','password1':'Password','passowrd2':'Confirm Password'}
        context = {'form': UserForm(),'expform':ExperienceForm(),'fquery':FacilitatorQueriesForm(),'place':personal_detail}
        return render(request, 'facilitators/register/index.html', context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        expform = ExperienceForm(request.POST)
        phone=request.POST.get('phone','')
        portfolio = request.FILES['pro']
        fquery=FacilitatorQueriesForm(request.POST)
        course=request.POST.get('course','')
        user=None
        if form.is_valid():
           user=form.save()
           profile=Profile.objects.get(user=user.id)
           profile.phone=phone
           profile.portfolio=portfolio
           profile.role=2
           profile.intrest=course
           profile.save()
       

        if expform.is_valid():
            ex=expform.save(commit=False)
            ex.facilitator=user
            ex.save()

        if fquery.is_valid():
            qo=fquery.save(commit=False)
            qo.user=user
            qo.save()
        
       
        
        
        #     #profile_form.save()
        #     messages.success(request, ('Your profile was successfully updated!'))
        #     return render(request, 'facilitators/index.html')
        # else:
        #     messages.error(request, ('Please correct the error below.'))
     
        return render(request, 'facilitators/index.html')