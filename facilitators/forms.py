from django.forms import ModelForm
from  facilitators.models import Facilitator,Experience
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class FacilitatorForm(ModelForm):
    class Meta:
        model = Facilitator
        fields = ('name', 'phone')
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['Linkedin_Url', 'Website_Url', 'Youtube_Url','RExperience','TExperience']

class FacilitatorRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )

    def save(self, commit=True):
        user = super( FacilitatorRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username=user.first_name+user.last_name
        if commit:
            user.save()

        return user

# class FacilitatorEditProfileForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = (
#             'email',
#             'first_name',
#             'last_name',
#             'password',
#             )


