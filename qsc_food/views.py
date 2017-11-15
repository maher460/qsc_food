# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import JsonResponse
from qsc_food.forms import SignUpForm
from qsc_food.models import *





# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.sex = form.cleaned_data.get('sex')
            user.profile.age = form.cleaned_data.get('age')
            user.profile.weight = form.cleaned_data.get('weight')
            user.profile.height = form.cleaned_data.get('height')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def food_database(request):
	user = request.user
	cuisines = list(Cuisine.objects.all())

	return render(request, 'food_database.html', {'cuisines': cuisines})


@login_required
def new_cuisine(request):

	if request.method == 'GET':
		return render(request, 'new_cuisine.html')

	if request.method == 'POST':
		data = request.POST
		print data

		cuisine_objs = list(Cuisine.objects.all())
		cuisines = map(lambda x: {'id': x.id, 'name': x.name}, cuisine_objs)
		return JsonResponse({'cuisines': cuisines})

	else:
		return JsonResponse({'error': 'Request is not POST'})
