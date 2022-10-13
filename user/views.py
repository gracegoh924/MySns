from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required



# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated # 인증된 사용자를 user에 저장한다.
        if user:
            return redirect('/') # 기본 페이지로 리다이렉트
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signup.html', {'error':'패스워드를 확인해주세요.'})
        else: # pw가 일치하면 하는 부분.
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error': '사용자 이름과 비밀번호는 필수항목입니다.'})
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error': '사용자가 존재합니다.'})
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')


def sign_in_view(request):

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/') # /라는 기본 url로 연결.
        else:
            return render(request, 'user/signin.html', {'error':'이름 혹은 패스워드를 확인해주세요.'})
            # return redirect('/login')

    elif request.method == 'GET': # 화면을 보여줄 때니까 get
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/user_list.html', {'user_list': user_list})


@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/user')