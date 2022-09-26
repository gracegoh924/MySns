from django.http import HttpResponse
from django.shortcuts import render # render: html 보여주는 역할


def base_response(request):
    return HttpResponse("안녕하세요! grace입니다!")

def first_view(request): # first_view() 함수는 'my_test.html' 보여주는 역할
    return render(request, 'my_test.html')

# 함수를 만들었으니 url과 연동해야. > urls.py
