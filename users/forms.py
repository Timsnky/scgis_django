from django import forms
from .models import UserProfile, Title, Country, MembershipLevel, PaymentMethod
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    title = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset = Title.objects.all(), empty_label="Select Title")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label = "First Name")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(label="About Me", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    organization = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    job_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    zip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    country = forms.ModelChoiceField(queryset = Country.objects.all(), empty_label="Select Country",widget=forms.Select(attrs={'class': 'form-control'}))
    listserv = forms.BooleanField(label="Add me to the SCGIS ListServ", required=False)
    public = forms.BooleanField(label="Make my profile Public", required=False)
    # membership_level = forms.ModelChoiceField(queryset = MembershipLevel.objects.all(), empty_label="Select Membership Level")
    # payment_method = forms.ModelChoiceField(label="How do you want to pay for your membership?*", queryset=PaymentMethod.objects.all(), empty_label="Select Payment Method")

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        password_confimation = cleaned_data.get("password_confirmation")

        if(password != password_confimation):
            raise forms.ValidationError("The passwords do not match")

        email = cleaned_data.get("email")
        if (User.objects.filter(email=email).exists()):
            raise forms.ValidationError("The email already exists in the system")

        return cleaned_data


class SignInForm(forms.Form):
    email = forms.CharField(label = "Email Address:", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



# class EditProfileForm(forms.Form):
    # organization = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    # job_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    # address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    # city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    # state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    # zip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = False)
    # country = forms.ModelChoiceField(queryset = Country.objects.all(), empty_label="Select Country",widget=forms.Select(attrs={'class': 'form-control'}))
    # listserv = forms.BooleanField(label="Add me to the SCGIS ListServ", required=False)
    # public = forms.BooleanField(label="Make my profile Public", required=False)
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required = False)
