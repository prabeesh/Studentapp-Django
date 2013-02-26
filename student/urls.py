from django.conf.urls.defaults import *
from student.views import mainpage, details, sort1, sort2, remove, search

urlpatterns = patterns('', 
    ('^$', mainpage),('^details/$', details),('^sort1/', sort1),('^sort2/$', sort2),('^remove/$', remove),('^search/$', search) 
)
