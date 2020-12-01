from django.conf.urls import url
from . import views

app_name="hello_word"

urlpatterns = [
    url('', views.hello_word, name='hello_word'),
]