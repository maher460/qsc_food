"""qsc_food_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from qsc_food import views as qsc_food_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', qsc_food_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^home/$', qsc_food_views.home, name='home'),
    url(r'^food_database/$', qsc_food_views.food_database, name='food_database'),

    url(r'^new_cuisine/$', qsc_food_views.new_cuisine, name='new_cuisine'),
    url(r'^select_cuisine/$', qsc_food_views.select_cuisine, name='select_cuisine'),

    url(r'^new_food/$', qsc_food_views.new_food, name='new_food'),

    url(r'^report/$', qsc_food_views.report, name='report'),

    #index page
    url(r'^', qsc_food_views.index, name='index'),
]