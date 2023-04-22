from rest_framework import serializers

from webapp.models import Photo, Favourite


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo', 'signature', 'author', 'created_at')


class FavouriteSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Favourite
        fields = ('user', 'photo', 'created_at')
