from rest_framework import generics, authentication, permissions, viewsets, mixins, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .serializers import UserSerializers, AuthTokenSerializer, CategorySerializer, ProductSerializer, StorageSerializer, ShopSerializer, ProductOnStorageSerializer

import sys

sys.path.append('..')
from main.models import Category, Product, Storage, Shop, ProductOnStorage


class CreateUserView(generics.CreateAPIView):
    """Create a new user"""
    serializer_class = UserSerializers


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializers
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


class StorageViewSet(viewsets.ModelViewSet):
    """Manage storages"""
    serializer_class = StorageSerializer
    queryset = Storage.objects.all()
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """Manage categories"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ShopViewSet(viewsets.ModelViewSet):
    """Manage shops"""
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductListCreateAPIView(APIView):
    """Manage products"""
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = Product.objects.all()
        serializer = ProductSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        category_id = request.data.get("category")['id']
        product_name = request.data.get("name")
        try:
            category = Category.objects.get(id=category_id)
            new_product = Product.objects.create(name=product_name, category=category)
            serializer = ProductSerializer(new_product)
            return Response(serializer.data, status=201)
        except:
            return Response(status=400)


class ProductDetailAPIView(APIView):
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        data = request.data
        product.name = data.get("name")
        product.save()
        category = Category.objects.get(id=data.get("category")['id'])
        category.product_set.add(product)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductAvailableListCreate(APIView):
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = ProductOnStorage.objects.all()
        serializer = ProductOnStorageSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        product_id = data.get("product")['id']
        product = Product.objects.get(id=product_id)
        product_on_storage = ProductOnStorage.objects.create(product=product)
        storage_ids = data.get("storage")
        shops_ids = data.get("shops")

        if storage_ids:
            for obj in storage_ids:
                storage_obj = get_object_or_404(Storage, pk=obj['id'])
                product_on_storage.storage.add(storage_obj)

        if shops_ids:
            for obj in storage_ids:
                storage_obj = get_object_or_404(Shop, pk=obj['id'])
                product_on_storage.shops.add(storage_obj)

        serializer = ProductOnStorageSerializer(product_on_storage)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductAvailableDetail(APIView):
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(ProductOnStorage, pk=pk)

    def get(self, request, pk):
        product_on_storage = self.get_object(pk)
        serializer = ProductOnStorageSerializer(product_on_storage)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        product_on_storage = self.get_object(pk)
        product_on_storage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








