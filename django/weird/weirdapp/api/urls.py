from django.conf.urls import include, url
from django.urls import path
from weirdapp.api import viewsets

app_name = 'weirdapp'

api_urls = [
    path('encode/', viewsets.EncodeViewSet.as_view()),
    path('decode/', viewsets.DecodeViewSet.as_view())
]