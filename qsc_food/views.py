# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import JsonResponse
from qsc_food.forms import SignUpForm
from qsc_food.models import *
import logging




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
    if request.method == 'GET':
        cuisines = list(Cuisine.objects.all())
        return render(request, 'food_database.html', {'cuisines': cuisines})

    elif request.method == 'POST':
        data = request.POST

        if type(data) != type(dict()): # could be a QueryDict
            data = dict(data)
            for k in data: # data is (k, [V]), make it (k, V)
                data[k] = data[k][0]

        logging.warning(data)

        new_plate = Plate(user_id=request.user.id)
        new_plate.save()

        if('part_1' in data and int(data['part_1']) != -1):
            new_part = Partition(plate_id=new_plate.id, food_id=int(data['part_1']))
            new_part.save()

        if('part_2' in data and int(data['part_2']) != -1):
            new_part = Partition(plate_id=new_plate.id, food_id=int(data['part_2']))
            new_part.save()

        if('part_3' in data and int(data['part_3']) != -1):
            new_part = Partition(plate_id=new_plate.id, food_id=int(data['part_3']))
            new_part.save()

        if('part_4' in data and int(data['part_4']) != -1):
            new_part = Partition(plate_id=new_plate.id, food_id=int(data['part_4']))
            new_part.save()

        return JsonResponse({'success': True})

    else:
        return JsonResponse({'success': False, 'error': 'Request is not GET or POST'})


@login_required
def new_cuisine(request):

    if request.method == 'GET':
        return render(request, 'new_cuisine.html')

    elif request.method == 'POST':
        data = request.POST

        if type(data) != type(dict()): # could be a QueryDict
            data = dict(data)
            for k in data: # data is (k, [V]), make it (k, V)
                data[k] = data[k][0]

        logging.warning(data)

        new_cuisine = Cuisine(name=str(data['cuisine_name']))
        new_cuisine.save()

        return JsonResponse({'success': True})

    else:
        return JsonResponse({'success': False, 'error': 'Request is not GET or POST'})


@login_required
def select_cuisine(request):

    if request.method == 'POST':

        data = request.POST

        if type(data) != type(dict()): # could be a QueryDict
            data = dict(data)
            for k in data: # data is (k, [V]), make it (k, V)
                data[k] = data[k][0]

        logging.warning(data)

        foods = list(Food.objects.filter(cuisine_id=int(data['cuisine_id'])))

        foods = map(lambda x: {'id': x.id, 'name': x.name}, foods)

        return JsonResponse({'success': True, 'foods': foods})

    else:
        return JsonResponse({'success': False, 'error': 'Request is not POST'})


@login_required
def new_food(request):

    if request.method == 'GET':
        return render(request, 'new_food.html')

    elif request.method == 'POST':
        data = request.POST

        if type(data) != type(dict()): # could be a QueryDict
            data = dict(data)
            for k in data: # data is (k, [V]), make it (k, V)
                data[k] = data[k][0]

        logging.warning(data)

        new_food = Food(name=str(data['food_name']),
                        calories=int(data['calories']),
                        fat=int(data['fat']),
                        protein=int(data['protein']),
                        fibre=int(data['fibre']),
                        sugar=int(data['sugar']), 
                        cuisine_id=int(data['cuisine_id']))
        new_food.save()

        return JsonResponse({'success': True})

    else:
        return JsonResponse({'success': False, 'error': 'Request is not GET or POST'})
