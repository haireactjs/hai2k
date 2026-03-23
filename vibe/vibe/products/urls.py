from django.urls import path
from . import views
from .views import ProductView

app_name = "products"
urlpatterns = [
    path('', ProductView.as_view(), name ='products'),
    # path('add', ProductView.as_view(), name ='add'),


]