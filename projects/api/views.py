from rest_framework import generics, viewsets
from ..models import Portfolio
from .serializers import PortfolioSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly


# class PortfolioListView(generics.ListAPIView):
#     queryset = Portfolio.objects.all()
#     serializer_class = PortfolioSerializer

class PortfolioListView(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
  
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)