from rest_framework import generics, status
from rest_framework.response import Response

from api.serializers import PhotoSerializer
from webapp.models import Photo, Favourite


class AddPhotoToFavouriteView(generics.CreateAPIView):
    serializer_class = PhotoSerializer

    def post(self, request, *args, **kwargs):
        photo = request.data.get('photo_id')
        user = request.user
        if not photo:
            return Response({'error': 'Фото с таким id не существует'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            photo = Photo.objects.get(pk=photo)
        except Photo.DoesNotExist:
            return Response({'error': 'Фото не найдено'}, status=status.HTTP_404_NOT_FOUND)
        if Favourite.objects.filter(user=user, photo=photo).exists():
            return Response({'error': 'Фото уже добавлено в избранное'}, status=status.HTTP_400_BAD_REQUEST)
        favourite = Favourite.objects.create(user=user, photo=photo)
        return Response(PhotoSerializer(favourite.photo).data, status=status.HTTP_201_CREATED)


class DeletePhotoFromFavouriteView(generics.DestroyAPIView):
    serializer_class = PhotoSerializer

    def delete(self, request, *args, **kwargs):
        photo = request.data.get('photo_id')
        user = request.user
        if not photo:
            return Response({'error': 'Фото с таким id не существует'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            favourite = Favourite.objects.get(user=user, photo__id=photo)
        except Favourite.DoesNotExist:
            return Response({'error': 'Не добавлено в избранное'}, status=status.HTTP_404_NOT_FOUND)
        favourite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
