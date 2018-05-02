# -*- coding: utf-8 -*-

# pylint: disable=invalid-name

from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect
from django.urls.base import reverse
import survey.views
import survey.forms
import django.contrib.auth.views

admin.autodiscover()


def home(request):
    """ Permit to not get 404 while testing. """
    return redirect(reverse("survey-list"))



urlpatterns = [
    url(r"^$", home, name="home"),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^survey/', include('survey.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'survey/login.html',
            'authentication_form': survey.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                
            }
        },
        name='login'),

]
