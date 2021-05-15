from django.db import models
from rest_framework import serializers
from ..models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ["id", "title", "description", "image_url"]
