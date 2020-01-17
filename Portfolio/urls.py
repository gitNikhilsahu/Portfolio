from django.urls import path
from Portfolio import views

urlpatterns = [
    path('', views.PortfolioView, name='portfolio_page'),
]
