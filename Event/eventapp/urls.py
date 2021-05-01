from django.urls import path
from . import views

app_name = "eventapp"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register', views.register, name='register'),
    # path('', views.subscribe, name="subscribe")

]