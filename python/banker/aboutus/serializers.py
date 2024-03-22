from rest_framework import serializers

from aboutus.models import AboutUsModel


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsModel
        fields =  fields = ['id', 'title', 'sub_description', 'image', 'sub_title', 'description']