from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from members.models import UserProfile


# Create your views here.
@login_required
def home(request):
    name = ''
    age = ''
    profile_picture = ''

    if UserProfile.objects.filter(user=request.user).exists():
        profile = UserProfile.objects.get(user=request.user)
        name = profile.name
        age = profile.age
        profile_picture = profile.profile_picture

    return render(request, 'core/home.html', {
        'name': name,
        'age': age,
        'profile_picture': profile_picture
    })


@login_required
def about(request):
    return render(request, 'core/about.html', {})


@login_required
def contact(request):
    return render(request, 'core/contact.html', {})

@login_required
def locations(request):
    return render(request, 'core/locations.html', {})

@login_required
def visitors(request):
    return render(request, 'core/visitors.html', {})
