from django.conf.urls import url
from app.views import *

urlpatterns=[
    url(r"^hello/",hello),
]