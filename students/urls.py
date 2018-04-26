from django.conf.urls import url
from students import views as students_views


app_name = 'students'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', students_views.student_detail, name='detail'),
    url(r'^add/$', students_views.student_add, name='student_add'),
    url(r'^remove/(?P<pk>[0-9]+)/$', students_views.student_remove, name='student_remove'),
    url(r'^edit/(?P<pk>[0-9]+)/$', students_views.student_edit, name='student_edit'),
    url(r'^$', students_views.list_view, name='list_view'),
]
