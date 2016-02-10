from django.conf.urls import patterns, include, url
from django.contrib import admin
import tokenizer

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^tokenizer/',include('tokenizer.urls')),
)
