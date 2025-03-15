from django.urls import path
from .views import CachedDataView

urlpatterns = [
    path('cached-data/', CachedDataView.as_view(), name='cached-data'),
]
