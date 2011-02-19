from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^search/', 'searchapp.views.searchview'),                       
)
