from rest_framework import viewsets
from .models import Product, User
from .serializers import ProductSerializer, UserSerializer
from django.shortcuts import render

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    return render(request, 'myapp/index.html')



