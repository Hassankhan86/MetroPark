from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required

def logoutUser(request):
    logout(request)
    return  redirect('accounts:login')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard:homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('dashboard:details')
            else:
                messages.info(request,"Username Or Password is Incorrect ")


    # return HttpResponse("ddasdasd")
    return render(request, 'accounts/login.html',)

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard:homepage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Accounts was created for ' + user)

                return redirect('accounts:login')

        context = {'form': form}
# return HttpResponse("Register")
    return render(request, 'accounts/register.html',context)
