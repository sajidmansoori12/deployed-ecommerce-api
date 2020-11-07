from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .serializers import ProductSerializer,BannerSerializer,OfferSerializer
from .models import Product,Banner,Offer

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class BannerView(viewsets.ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()

class OfferView(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()