from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from api.serializers import PhotoSerializer, FavouriteSerializer
from webapp.models import Photo, Favourite


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.filter(is_deleted=False)
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        publication = serializer.instance
        if publication.user == self.request.user:
            serializer.save()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.user == user:
            instance.delete()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.user == user:
            instance.delete()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
