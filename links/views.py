from rest_framework import generics, permissions
from .models import Links
from .serializer import LinksSerializer


class LinksCreateView(generics.CreateAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        link_id = self.request.data.get('link_id')

        # Check if link_id exists
        if link_id:
            try:
                link_instance = Links.objects.get(id=link_id, created_by=self.request.user)
                print(self.request.user)
                # If link exists, update its details
                serializer.update(link_instance, self.request.data)
            except Links.DoesNotExist:
                # If link_id does not exist for this user, create a new link
                serializer.save(created_by=self.request.user)
        else:
            # If no link_id is provided, create a new link
            serializer.save(created_by=self.request.user)


class UserLinksListView(generics.ListAPIView):
    serializer_class = LinksSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Links.objects.filter(created_by=self.request.user)