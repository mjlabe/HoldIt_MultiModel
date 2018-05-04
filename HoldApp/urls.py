from django.conf.urls import url
from HoldApp.views import views_public, views_users, views_contrib
from django.urls import path, include


urlpatterns = [
    url(r'^report/$', views_contrib.new_report, name='new_report'),
    url(r'^$', views_public.index, name='index'),
    url(r'^$', views_public.header, name='header'),
    url(r'^$', views_public.footer, name='footer'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^registration/signup/$', views_public.signup, name='signup'),

]
