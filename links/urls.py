from django.urls import path
from .views import LinksCreateView, UserLinksListView, SharedUserLinksListView

urlpatterns = [
    path('create-link', LinksCreateView.as_view(), name='create-link'),
    path('user-links', UserLinksListView.as_view(), name='user-links'),
    path('user-links/<int:user_id>', SharedUserLinksListView.as_view(), name='shared-user-links'),
]
