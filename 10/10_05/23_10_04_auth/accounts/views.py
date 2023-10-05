from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method=='POST':
        # username, password 받아와서 DB에 있는거랑 비교하고
        # 로그인성공하면 session에 user정보 넣어주기
        # >>>> 이   걸 장고가 대신해줍니다. 
        form = AuthenticationForm(request,request.POST)
        next = request.GET.get('next')
        if form.is_valid(): # 사용자가 username과 password를 제대로 입력했다면
            auth_login(request,form.get_user())    # 실제 로그인 처리하기
            return redirect(next or 'articles:index')
    # 로그인할 수 있는 화면을 제공
    # 로그인 로직을 장고가 처리할거기 때문에
    # ID/PW 입력받는 form을 장고가 만들어 놓은 form을 사용해야 합니다. 
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request,'accounts/login.html',context)


@login_required
def logout(request):
    if request.method=='POST':
        auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(data=request.POST,instance=request.user)
        if form.is_valid():
            user = form.save()
            # update_session_auth_hash(request,user)
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request,pk):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(user=request.user)
    context={
        'form' : form
    }
    return render(request, 'accounts/change_password.html',context)

