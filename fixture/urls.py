from django.urls import path, include
from .views import FixtureViewSet
# Create a router and register our viewsets with it.

fixture_list = FixtureViewSet.as_view({
    'get': 'list'
})
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', fixture_list, name='fixture-list'),
]