from rest_framework import serializers

from gallery.models import GalleryCategoryModel, GalleryModel



class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryModel
        fields = '__all__'

class GalleryCategorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = GalleryCategoryModel
        fields = '__all__'