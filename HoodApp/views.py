from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Profile
# from .forms import ProfleForm
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

