from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.TestView.as_view(), name='home'),
    path('radios/', views.RadioViewSet.as_view(), name='radios'),
]
