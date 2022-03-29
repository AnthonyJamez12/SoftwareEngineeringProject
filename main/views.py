from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from itsdangerous import Serializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .forms import *
from .models import *
from .serializers import *

# Create your views here.





@api_view(['POST'])
def post_create_view(request, *args, **kwargs):
    serializer = UploadsSerializer(data = request.POST)
    if serializer.is_valid(raise_exception = True):
        serializer.save(user = request.user)
        return Response(serializer.data, status = 201)
    return Response({}, status = 400)
#########Look above at the serilaization it should be uploadscreateserializwer but i dont have the

@api_view(['GET'])
def post_detail_view(request, post_id, *args, **kwargs):
    query_set = Uploads.objects.filter(id = post_id)
    if not query_set.exists():
        return Response({}, status = 404)
    object = query_set.first()
    serializer = UploadsSerializer(object)
    return Response(serializer.data, status = 200)




@api_view(['GET'])
def post_display_all_view(request, *args, **kwargs):
    query_set = Uploads.objects.all()
    serializer = UploadsSerializer(query_set, many = True)
    return Response(serializer.data)












@api_view(['POST', 'GET'])
def home(request):
    return redirect(reverse("profile", args=[request.user]))




@api_view(['POST', 'GET'])
def profile(request, user):
    img = Uploads.objects.filter().order_by("-id")
    #profile = Profile.objects.filter(user = request.user).first()
   

    #serializer = ProfileSerializer(profile)
    serializer = UploadsSerializer(img, many = True)
    return Response(serializer.data, )






@api_view(['POST', 'GET'])
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

        serializer = ProfileSerializer(profile)
        serializer_2 = UploadsSerializer(img, many = True)
        return Response({'Profile': serializer.data, 'Uploads': serializer_2.data})




@api_view(['POST', 'GET'])
def profile_search_view(request, *args, **kwargs):
    context = {}
    if request.method == "Get":
        search_query = request.GET.get("q")
        if len(search_query) > 0:
            search_results = Profile.onjects.filter(user__username__icontains=search_query).distinct()
            user = request.user
            profiles = []
            for profile in search_results:
                profiles.append((profile, False))
            context['profiles'] = profiles
        
            #serializer = ProfileSerializer(search_results)
            #return Response(serializer.data, status = 200)
    #serializer = ProfileSerializer(search_results)
    #return Response(serializer.data, status = 200)


    
    



@api_view(['POST', 'GET'])
def profile_uploads(request):
    #profile = request.user.profile
    #if request.method == "POST":
        #form = Uploads_Form(data = request.POST, files = request.FILES)
        #if form.is_valid():
            #form.instance.profile = request.user.profile
            #form.save()
            #obj = form.instance
            #return redirect(reverse("profile", args=[request.user]))
    #else:
        #form = Uploads_Form()
    #img = Uploads.objects.all()
    #context = {"img":img, "form":form, "profile": profile}
    #return render(request,"main/profile_uploads.html", context)
    serializer = UploadsSerializer(data = request.POST)
    if serializer.is_valid(raise_exception = True):
        serializer.save(user = request.user)
        return Response(serializer.data, status = 201)
    return Response({}, status = 400)




@api_view(['POST', 'GET'])
def profile_settings(request, user):
    profile = Profile.objects.filter(user = request.user).first()

    form = Profile_Form(instance = profile)
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES,instance = profile)
        if form.is_valid():
            form.save()
    context = {"profile": profile, "form": form}
    return render(request, 'main/profile_settings.html', context)


@api_view(['POST', 'GET'])
def single_page(request, id):
    img = Uploads.objects.filter(id = id).first()
    profile = Uploads.objects.filter(id = request.user.id)

    context = { "img": img, "profile": profile}

    return render(request, "main/single_page.html", context)


@api_view(['POST', 'GET'])
def single_page_visit(request, id):
    img = Uploads.objects.filter(id = id).first()
    profile = Uploads.objects.filter(id = request.user.id)

    context = { "img": img, "profile": profile}

    return Response({'Profile': serializer.data, 'Uploads': serializer_2.data})



@api_view(['POST', 'GET'])
def delete_photo(request, id):
    if request.method == 'POST':
        img = Uploads.objects.get(id = id)
        img.delete()
    return Response({"message": "Post removed"}, status=200)




@api_view(['POST', 'GET'])
def make_account(request):
    return render(request, "main/make_account.html", )
