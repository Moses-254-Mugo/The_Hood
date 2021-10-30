from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,PostForm, BusinessForm, CommentForm
from django.http import HttpResponseRedirect
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        current_user = request.user
        # profile = Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')
    return render(request,'index.html')


@login_required(login_url='/accounts/login/')
def myProfile(request):
    current_user= request.user
    profiles =Profile.objects.get(username=current_user)
    return render(request, 'user_profile.html', {'profiles':profiles})

@login_required(login_url='/accounts/login/')
def New_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:

        form = ProfileForm()
    return render(request, 'profile_form.html',{'form': form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            profile = form.save(commit =False)
            profile.username = current_user
            profile.save()

        return redirect('index')
    elif Profile.objects.get(username = current_user):
        profile = Profile.objects.get(username = current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()
    
    return render(request, 'profile_update.html', {'form': form})
    