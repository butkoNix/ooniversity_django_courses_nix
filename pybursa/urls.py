from django.conf.urls import include, url
from django.contrib import admin
from pybursa import views as pybursa_views
from courses import views as courses_views
from students import views as students_views

urlpatterns = [
    url(r'^$', pybursa_views.index, name='index'),
    url(r'^contact/$', pybursa_views.contact, name='contact'),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^courses/(?P<pk>[0-9]+)/', courses_views.courses, name='courses'),
    url(r'^student/(?P<pk>[0-9]+)/', students_views.student_detail, name='student_detail'),
    url(r'^student/$', students_views.student_list, name='student_list'),

    url(r'^admin/', admin.site.urls),
]