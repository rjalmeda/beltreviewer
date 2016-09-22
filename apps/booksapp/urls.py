from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addbook$', views.addbook),
    url(r'^createbook$', views.createbook),
    url(r'^bookreviews/(?P<bookid>\w*)$', views.bookreviews),
    url(r'^addreview$', views.addreview),
    url(r'^displayallbooks$', views.displayallbooks)
]