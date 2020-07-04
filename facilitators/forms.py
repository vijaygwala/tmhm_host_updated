from django.forms import ModelForm
from  facilitators.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name','username', 'email', 'password1', 'password2', )
    
     
# class FacilitatorForm(ModelForm):
#     class Meta:
#         model = Facilitator
#         fields = ('name', 'phone')
# class ExperienceForm(ModelForm):
#     class Meta:
#         model = Experience
#         fields = ['Linkedin_Url', 'Website_Url', 'Youtube_Url','RExperience','TExperience']

# # class FacilitatorQueriesForm(ModelForm):
# #     class Meta:
# #         model=FacilitatorQueries
# #         fields=('query','status')
# # class FacilitatorEditProfileForm(UserChangeForm):

# #     class Meta:
# #         model = User
# #         fields = (
# #             'email',
# #             'first_name',
# #             'last_name',
# #             'password',
# #             )

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email','username')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'phone', 'portfolio')

