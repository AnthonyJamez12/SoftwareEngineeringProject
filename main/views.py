from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

# Create your views here.
#img = Uploads.objects.all()

def home(request):
    return redirect(reverse("profile", args=[request.user]))




def profile(request, user):
    img = Uploads.objects.filter(profile_id = request.user.profile).order_by("-id")
    profile = Profile.objects.filter(user = request.user).first()
    context = {"profile": profile, "img": img}

    return render(request, "main/profile.html", context)







def profile_view(request, username, *args, **kwargs,):
    context = {}
    try:
        user = User.objects.get(username=username)
        profile = user.profile
        img = profile.uploads_set.all().order_by("-id")

        context['username'] = user.username
    except:
        return HttpResponse("Something went wrong.")
    if profile:
        context = {"profile": profile, "img": img}

        return render(request, "main/profile_visit.html", context)




def profile_search_view(request, *args, **kwargs):
	context = {}
	if request.method == "GET":
		search_query = request.GET.get("q")
		if len(search_query) > 0:
			search_results = Profile.objects.filter(user__username__icontains=search_query).distinct()
			user = request.user
			profiles = [] # [(profile1, True), (profile2, False), ...]
			for profile in search_results:
				profiles.append((profile, False)) # you have no friends yet
			context['profiles'] = profiles

	return render(request, "main/search_results.html", context)




def profile_uploads(request):
    profile = request.user.profile
    if request.method == "POST":
        form = Uploads_Form(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.instance.profile = request.user.profile
            form.save()
            obj = form.instance
            return redirect(reverse("profile", args=[request.user]))
    else:
        form = Uploads_Form()
    img = Uploads.objects.all()
    #profile = Profile.objects.filter(user = request.user).first()
    context = {"img":img, "form":form, "profile": profile}
    return render(request,"main/profile_uploads.html", context)




def profile_settings(request, user):
    profile = Profile.objects.filter(user = request.user).first()

    form = Profile_Form(instance = profile)
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES,instance = profile)
        if form.is_valid():
            form.save()
    context = {"profile": profile, "form": form}
    return render(request, 'main/profile_settings.html', context)


def single_page(request, id):
    img = Uploads.objects.filter(id = id).first()
    profile = Uploads.objects.filter(id = request.user.id)

    context = { "img": img, "profile": profile}

    return render(request, "main/single_page.html", context)



def single_page_visit(request, id):
    img = Uploads.objects.filter(id = id).first()
    profile = Uploads.objects.filter(id = request.user.id)

    context = { "img": img, "profile": profile}

    return render(request, "main/single_page_visit.html", context)




def delete_photo(request, id):
    if request.method == 'POST':
        img = Uploads.objects.get(id = id)
        img.delete()

    return redirect(reverse("profile", args=[request.user]))

def make_account(request):
    return render(request, "main/make_account.html", )
