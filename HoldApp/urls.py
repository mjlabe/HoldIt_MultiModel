from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^report/$', views.new_report, name='new_report'),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.header, name='header'),
    url(r'^$', views.footer, name='footer'),
]
