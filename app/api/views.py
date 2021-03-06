from rest_framework import generics, authentication, permissions, viewsets, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .serializers import UserSerializers, AuthTokenSerializer, CategorySerializer, ProductSerializer, StorageSerializer

import sys

sys.path.append('..')
from main.models import Category, Product, Storage


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


class CategoryGenericAPIView(generics.GenericAPIView, mixins.UpdateModelMixin,
                             mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    """Get, update and delete a category"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class CategoryList(generics.ListCreateAPIView):
    """Create category and list all"""
    serializer_class = CategorySerializer
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()


# class ProductsView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response({"Products": serializer.data})
#
class ProductsView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        category = get_object_or_404(Category, id=self.request.data.get('category'))
        return serializer.save(category=category)


class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class StorageViewSet(viewsets.ModelViewSet):
    serializer_class = StorageSerializer
    queryset = Storage.objects.all()
    authentication_classes = [authentication.BasicAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
