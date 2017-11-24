from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

# Create a router and register viewsets with it; DefaultRouter class automatically creates the API root view
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Pastebin API')

# The API URLs are now determined automatically by the router; additionally, included the login URLs for the browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


"""
# Deprecated when adding viewsets classes, unlike View classes, don't require manually designing the URL configuration

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

# auth pattern used to include login and logout views for browsable API
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))
]
"""
