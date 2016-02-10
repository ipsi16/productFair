from django.conf.urls import patterns, include, url
import views

urlpatterns=patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^question$', views.question, name='question'),
	url(r'^answer$', views.answer, name='answer'),
)

