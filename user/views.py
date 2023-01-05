
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from user.models import CustomUser
from codes.forms import CodeForm
from django.contrib.auth import login
from django.contrib import messages
from verify.utils import send_sms
# Create your views here.

def Home(request):
    return render(request, 'main.html')
@login_required(login_url='/login')
def Authorizeonly(request):
    return HttpResponse('this is for authorized people only')
def auth_view(request):
    form=AuthenticationForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            request.session['pk']=user.pk
            return redirect(verify_view)

            
    return render(request, 'auth.html',{'form':form})

def verify_view(request):
    form=CodeForm(request.POST or None)
    pk=request.session.get('pk')
    if pk:
        user=CustomUser.objects.get(pk=pk)
        code=user.codes
        code_user=f"{user.username}:{user.codes}"
        if not request.POST:
            send_sms(code_user, user.phone_number)
            
        if form.is_valid():
            num=form.cleaned_data.get('number')
            if str(code)==num:
                code.save()
                login(request, user)
                return redirect(Authorizeonly)
            else:
                
                return redirect(auth_view)
    return render(request,'verify.html',{'form':form})    
        
    