from django.conf.urls import patterns, url

from foodonthemove import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
