from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def show_demo_page(request):
    return render(request, 'hub_template/index.html')
    #return render(request, 'index.html')


def show_login_page(request):
    return render(request, 'login_page.html')

def dologin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Methon Not allowd</h2>")
    else :
        #user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        user = authenticate(request, username = request.POST.get("username"),password=request.POST.get("password") )
        if user != None :
            login(request,user)
            if user.user_type=='1':
                #return HttpResponse("Username : "+ request.POST.get('username')+ " Password : " + request.POST.get('password'))
                return HttpResponseRedirect('/admin_home')
            elif user.user_type =='2':
                return HttpResponseRedirect('/stuff')
        else :
            messages.error(request, 'معلومات التسجيل غير صحيحة')
            return HttpResponseRedirect('/')

def get_user_details(request):
    if request.user.is_authenticated  :
        return HttpResponse("User : "+ request.user.email+ " usertype : "+str(request.user.user_type))
    else :
        return HttpResponseRedirect('/')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
    #return HttpResponse("<h2>Methon Not allowd</h2>")
