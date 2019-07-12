from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.generic import CreateView
from django.template import RequestContext
from django.shortcuts import render_to_response
from decimal import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
import datetime
import csv
from django.views.decorators.csrf import csrf_exempt

from app.forms import UserForm,CodeForm
from app.models import *
# Create your views here.


def index(request):
    """
    Index view for homepage for logged in as well as logged out users
    :param request:
    :return:
    """
    return render(request, "index.html")


def user_login(request):
    """
    Login View
    :param request:
    :return:
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect("/home")
    error = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                next_url = request.GET.get('next', '/home')
                return HttpResponseRedirect(next_url)
        else:
            error = True

    return render(request, "login.html", {'error':error})


def user_register(request):
    """
    Register a new user
    :param request:
    :return:
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect("/home")
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_profile = UserProfile.objects.create(user=user)
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request,
                  'register.html',
                  {'user_form': user_form, 'registered': registered})


@login_required(login_url='/login')
def home(request):
    """
    User login
    :param request:
    :return:
    """
    if request.user.is_authenticated():
        codes = Code.objects.filter(user=request.user).order_by('-created_at')
        for code in codes:
            acount = Annotations.objects.filter(code=code).count()
            code.acount = acount
            code.lent = len(code.code)
        return render(request,"home.html",{'codes':codes})
    raise Http404

@login_required(login_url='/')
def logout_user(request):
    """
    Logout
    :param request:
    :return:
    """
    logout(request)
    next_url = request.GET.get('next', '/')
    return HttpResponseRedirect(next_url)


@login_required(login_url='/login')
def add_code(request):
    """
    For adding new code entries
    :param request:
    :return:
    """
    if request.method == 'POST':
        cf = CodeForm(data=request.POST)
        if cf.is_valid():
            ok = cf.save(commit=False)
            ok.user = request.user
            ok.save()
            next_url = request.GET.get('next', '/code/'+str(ok.id))
            return HttpResponseRedirect(next_url)
        else:
            print cf.errors
    else:
        cf = CodeForm()
    return render(request,"add.html",{'form':cf})

@login_required(login_url='/login')
@csrf_exempt
def add_annotation(request):
    if request.user.is_authenticated():
        if request.POST:
            codeid = request.POST.get('codeid')
            title = request.POST.get('title')
            content = request.POST.get('content')
            color = request.POST.get('color')
            start = request.POST.get('start')
            end = request.POST.get('end')
            if codeid and title and content and color and start and end:
                # try:
                code = Code.objects.get(id=int(codeid))
                if code.user == request.user :
                    ann = Annotations()
                    ann.code = code
                    ann.title = title
                    ann.content = content
                    ann.color = color
                    ann.start = int(start)
                    ann.end = int(end)-int(start)+1
                    ann.save()
                    return HttpResponse("success")
                else:
                    return HttpResponse('code does not belong to user')
                # except:
                #     return HttpResponse('code does not exist')
            else:
                return HttpResponse("error")
    raise Http404


def view_code(request, codeid):
    """
    Display the code
    :param request:
    :param codeid:
    :return:
    """
    try:
        code = Code.objects.get(id=codeid)
        annotations = Annotations.objects.filter(code=code).order_by('start')
        owner = False
        if request.user.is_authenticated():
            if request.user == code.user:
                owner = True
        #apply annotations to
    except:
        raise Http404
    return render(request,"code.html",{'code':code.code,'title':code.title,'anno':annotations,'lang':code.language,'owner':owner,'cid':code.id})

@login_required(login_url='/login')
def delete_code(request, codeid):
    """
    Display the code
    :param request:
    :param codeid:
    :return:
    """
    try:
        code = Code.objects.get(id=codeid)
        if request.user.is_authenticated():
            if request.user == code.user:
                code.delete()
                return HttpResponse("deleted!")
            else:
                return HttpResponse("code does not belong to the user")
        #apply annotations to
    except:
        return HttpResponse("error Deleting")