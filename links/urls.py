from django.urls import path
from .views import LinksCreateView, UserLinksListView

urlpatterns = [
    path('create-link', LinksCreateView.as_view(), name='create-link'),
    path('user-links', UserLinksListView.as_view(), name='user-links'),
]
