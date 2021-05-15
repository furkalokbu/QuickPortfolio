from rest_framework import generics
from ..models import Portfolio
from .serializers import PortfolioSerializer


class PortfolioListView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
