from django.contrib import admin
from django.urls import path, include
# If we want to authenticate users via a framework like flutter, vue etc
# we need a login page with user and password
# and  if it checks we return the token to the user
# there is view in rest framework that helps us do that
from rest_framework.authtoken.views import obtain_auth_token
# this view will return the token when we logging that user
urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token', obtain_auth_token, name='obtain-token'),
    # #path('', include('radio_api.urls')),
    path('', include('snippets.urls')),
    path('', include('snippets.urls')),
    path('admin/', admin.site.urls),
]
