
from django.conf.urls import url, include
from django.contrib import admin
from audio_service.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index),
]
