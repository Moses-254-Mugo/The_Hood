from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,PostForm, BusinessForm, CommentForm
from django.http import HttpResponseRedirect
from .models import Health, Profile, Police,Post,Business
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

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
    profiles=Profile.objects.filter( user_id=current_user.id).first()
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
        instance = Profile.objects.filter(user_id=current_user.id).first()
        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            profile = form.save(commit =False)
            profile.username = current_user
            profile.save()

        return redirect('index')
    elif Profile.objects.filter( user_id=current_user.id).exists():
        profile = Profile.objects.filter( user_id=current_user.id).first()
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()
    
    return render(request, 'profile_update.html', {'form': form})

@login_required(login_url='/accounts/login/')
def well_being(request):
    current_user = request.user
    profile = Profile.objects.filter( user_id=current_user.id).first()
    health = Health.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'health.html', {'health':health})

@login_required(login_url='/accounts/login/')
def authorities(request):
    current_user = request.user
    profile = Profile.objects.filter( user_id=current_user.id).first()
    authorities = Police.objects.filter(neighbourhood = profile.neighbourhood) 

    return render(request, 'authorities.html',{'authorities': authorities})

@login_required(login_url='/accounts/login/')
def posts(request):
    current_user = request.user
    profile=Profile.objects.filter( user_id=current_user.id).first()
    post = Post.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'post.html', {'post':post})

@login_required(login_url='/accounts/login/')
def Newpost(request):
    current_user = request.user
    profile=Profile.objects.filter( user_id=current_user.id).first()

    if request.method=="POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.username = current_user
            post.neighbourhood = profile.neighbourhood
            post.post_img = profile.image
            post.save()
        
        return HttpResponseRedirect('/post')
    else:
        form = PostForm()

    return render(request, 'post-form.html',{'form':form})

@login_required(login_url='/accounts/login/')
def business(request):
    current_user=request.user
    profile=Profile.objects.filter( user_id=current_user.id).first()
    business =Business.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'business.html',{'business':business})

@login_required(login_url='/accounts/login/')
def create_new_business(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)

    if request.method=="POST":
        form= BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.neighbourhood = profile.neighbourhood
            business.save()
            
        return HttpResponseRedirect('/business')
    else:
        form = BusinessForm()
    return render(request, 'business_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    if 'post' in request.GET and request.GET["post"]:
         search_term = request.GET.get("post")
         searhed_post = Post.search_post(search_term)
         message = f'{search_term}'

         print(searhed_post)

         return render(request, 'search.html', {'message':message, 'post': searhed_post, 'profile': profile})
    else:
        message= 'You have not search for any term'
        return render(request, 'search.html', {'message':message})