from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfleForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        current_user = request.user
        profile = Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')
    return redirect(request, 'index.html')


@login_required(login_url='/accounts/login/')
def myProfile(request):
    current_user= request.user
    profiles =Profile.objects.get(username=current_user)
    return render(request, 'profile/user_profile.hmtl', {'profiles':profiles})


# def search_results(request):

#     if 'article' in request.GET and request.GET["article"]:
#         search_term = request.GET.get("article")
#         searched_articles = Article.search_by_title(search_term)
#         message = f"{search_term}"

#         return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-news/search.html',{"message":message})