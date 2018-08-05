from django.urls import path

from . import views

app_name = 'companies'
urlpatterns = [
    path('api/', views.StockList.as_view(), name = 'api'),
]