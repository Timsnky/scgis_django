#Imports
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserProfile
from .forms import RegisterForm, SignInForm
from .models import Title, Country, PaymentMethod, MembershipLevel
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
from django.contrib import messages, auth

# Methods
def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/signin')
    userProfiles = UserProfile.objects.all()
    context = {
        'userProfiles': userProfiles
    }
    return render(request, 'users/index.html', context)

def profile(request, user_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/signin')
    user = get_object_or_404(UserProfile, pk=user_id)
    return render(request, 'users/profile.html', {'user': user})

def registerStart(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            # Create the User
            user = User()
            user.email = registerForm.cleaned_data['email']
            user.first_name = registerForm.cleaned_data['first_name']
            user.last_name = registerForm.cleaned_data['last_name']
            user.set_password(registerForm.cleaned_data['password'])
            user.username = registerForm.cleaned_data['email']
            user.save()

            userProfile = UserProfile()
            userProfile.user = user
            userProfile.title = registerForm.cleaned_data['title']
            userProfile.organization = registerForm.cleaned_data['organization']
            userProfile.job_title = registerForm.cleaned_data['job_title']
            userProfile.city = registerForm.cleaned_data['city']
            userProfile.state = registerForm.cleaned_data['state']
            userProfile.zip = registerForm.cleaned_data['zip']
            # userProfile.membership_level = registerForm.cleaned_data['membership_level']
            userProfile.country = registerForm.cleaned_data['country']
            # userProfile.payment_method = registerForm.cleaned_data['payment_method']
            userProfile.listserv = registerForm.cleaned_data['listserv']
            userProfile.public = registerForm.cleaned_data['public']
            userProfile.bio = registerForm.cleaned_data['bio']
            userProfile.save()

            messages.success(request, "You have successfully registered to SCGIS")
            return HttpResponseRedirect('/')
        else:
            messages.error("User not created")
    else:
        registerForm = RegisterForm()

    return render(request, "users/register_start.html", {'registerForm': registerForm})

def signIn(request):
    if(request.method == 'POST'):
        signInForm = SignInForm(request.POST)
        if(signInForm.is_valid()):
            email = signInForm.cleaned_data['email']
            password = signInForm.cleaned_data['password']
            user = auth.authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, "You have successfully been logged in")
                    return HttpResponseRedirect('/')
                else:
                     messages.error(request, "Your account is not yet active")
            else:
                messages.error(request, "Invalid email/password")
    else:
        signInForm = SignInForm()
    return render(request, 'users/signin.html', {'signInForm': signInForm})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def edit(request, id):
    userProfiles = UserProfile.objects.all()
    context = {
        'userProfiles': userProfiles
    }
    return render(request, 'users/index.html', context)
    # userProfile = get_object_or_404(UserProfile, id=id)
    # if request.method == 'POST':
    #     editForm = EditProfileForm(request.POST, instance = userProfile)
    #     if editForm.is_valid():
    #         userProfile = editForm.save(commit=False)
    #         userProfile.save()
    #         messages.success(request, "You have successfully updated your profile")
    #         return HttpResponseRedirect('/users/profile/'+userProfile.id)
    #     else:
    #         messages.error("User profile not saved")
    # else:
    #     editForm = EditProfileForm(instance = userProfile)
    # context = {
    #     'editForm': editForm,
    #     'userProfile': userProfile
    # }
    # return render(request, "users/editprofile.html", context)