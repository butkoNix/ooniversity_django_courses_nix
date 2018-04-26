from django.conf.urls import url
from courses import views as courses_views


app_name = 'courses'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', courses_views.detail, name='detail'),
    url(r'^add/$', courses_views.course_add, name='course_add'),
    url(r'^remove/(?P<pk>[0-9]+)/$', courses_views.course_remove, name='course_remove'),
    url(r'^edit/(?P<pk>[0-9]+)/$', courses_views.course_edit, name='course_edit'),
    url(r'^$', courses_views.list_view, name='list_view'),
]
