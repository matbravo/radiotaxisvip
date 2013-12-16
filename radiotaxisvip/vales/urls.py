from django.conf.urls import patterns, url
from vales import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^agregar/$', views.agregar, name='agregar'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^agregar_mod/$', views.agregar_mod, name='agregar_mod'),
    url(r'^cambiar_estado/$', views.cambiar_estado, name='cambiar_estado'),
    url(r'^verificar/$', views.verificar, name='verificar'),
    url(r'^verificar/(?P<vale_id>\d+)/verificar_vale/$', views.verificar_vale, name='verificar_vale'),
)