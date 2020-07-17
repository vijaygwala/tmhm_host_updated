from django.forms import ModelForm
from  facilitators.models import *
from myauth.models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms



class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta: 
        model = CustomUser
        fields = ( 'first_name', 'last_name', 'email', 'password1', 'password2' )
    def save(self, commit = True): 
        user = super(UserForm, self).save(commit = False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
     
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['Linkedin_Url', 'Website_Url', 'Youtube_Url','RExperience','TExperience']
    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        self.fields['Linkedin_Url'].widget.attrs.update({'placeholder': 'Linkedin Url'})
        self.fields['Website_Url'].widget.attrs.update({'placeholder': 'Website Url'})
        self.fields['Youtube_Url'].widget.attrs.update({'placeholder': 'Youtube Url'})
        

class FacilitatorQueriesForm(ModelForm):
    class Meta:
        model=FacilitatorQueries
        fields=('query',)
    def __init__(self, *args, **kwargs):
        super(FacilitatorQueriesForm, self).__init__(*args, **kwargs)
        self.fields['query'].widget.attrs.update({'placeholder': 'Ask Your Question','id':'autoresizing'})
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'phone',)

