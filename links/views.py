from rest_framework import generics, permissions
from .models import Links
from .serializer import LinksSerializer


class LinksCreateView(generics.CreateAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UserLinksListView(generics.ListAPIView):
    serializer_class = LinksSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Links.objects.filter(created_by=self.request.user)