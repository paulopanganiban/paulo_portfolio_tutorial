from django.conf.urls import url
from . import views

app_name="hello_word"

urlpatterns = [
    url('hello_world/', views.hello_word, name='hello_word'),
]