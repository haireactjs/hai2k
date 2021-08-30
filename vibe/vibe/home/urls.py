from django.urls import path
from . import views
from .views import HomeView, AboutView

app_name = "home"
urlpatterns = [
    path('', HomeView.as_view(), name ='home'),
    path('about/', AboutView.as_view(), name ='about')

]