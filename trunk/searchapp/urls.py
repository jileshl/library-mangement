from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^search/searchResult', 'searchapp.views.searchresult'),
    (r'^search/', 'searchapp.views.searchview'),
                       
)
