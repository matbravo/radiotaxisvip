from django.conf.urls import patterns, url

from vales import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^administracion', views.administracion, name='administracion'),
    url(r'^locucion', views.locucion, name='locucion'),
    url(r'^contabilidad', views.contabilidad, name='contabilidad'),
    url(r'^logout', views.logout_user, name='logout'),
    
)