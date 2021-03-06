from django.db import models
from django.http import request
from rest_framework import serializers
from ..models import Portfolio, Image


# class PortfolioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Portfolio
#         fields = ["id", "title", "description", "image"]

class ImagesListView(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['title']

class PortfolioSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField(read_only=True)
    portfolio = ImagesListView(many=True, read_only=True)
    # custom = ImagesListView(many=True, read_only=True)
    
    class Meta:
        model = Portfolio
        # exclude = ["updated_at", "show",] 
        fields = ["author", "portfolio", "thumbnail", "created_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d %Y")

    def get_thumbnail(self, obj):
        if bool(obj.thumbnail):
            return self.context['request'].build_absolute_uri(obj.thumbnail.url)