from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('snippets/', views.snippet_list, name='snippests'),
    path('snippets/<int:pk>/', views.snippet_detail, name='snippest-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
