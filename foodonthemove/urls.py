from django.conf.urls import patterns, url

from foodonthemove import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^list_ticket/$', views.list_ticket, name='list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login')
)
