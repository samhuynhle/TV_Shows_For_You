from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^shows/new$',views.add),
    url(r'^shows$',views.all_shows),
    url(r'^shows/(?P<show_id>[0-9]+)/edit$',views.edit_show),
    url(r'^shows/(?P<show_id>[0-9]+)/delete$',views.delete_show),
    url(r'^shows/(?P<show_id>[0-9]+)/',views.display_show),
    url(r'^edit_process$',views.edit_process),
    url(r'^add_process$',views.add_process),
    url(r'^$',views.home),
]
