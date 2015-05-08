from django.conf.urls import patterns, url

from tables_test import views

urlpatterns = patterns('',
    url(r'^$', views.people, name='people'),
)