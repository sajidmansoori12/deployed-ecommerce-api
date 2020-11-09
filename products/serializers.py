from rest_framework import serializers

from .models import Product,Banner,Offer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','description','price','image','category','featured','rating')


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('banner_image','banner_name')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('offer_image','offer_name','type')