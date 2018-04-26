from django.conf.urls import include, url
from django.contrib import admin
from pybursa import views as pybursa_views

admin.site.site_header = 'PyBursa Administration'

urlpatterns = [
    url(r'^$', pybursa_views.index, name='index'),
    url(r'^contact/$', pybursa_views.contact, name='contact'),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^coaches/', include('coaches.urls')),

    url(r'^admin/', admin.site.urls),
]
