from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'api'

router = DefaultRouter()
router.register('storages', views.StorageViewSet, basename='storages')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('shops', views.ShopViewSet, basename='categories')

urlpatterns = router.urls

urlpatterns = [
    path('user/create/', views.CreateUserView.as_view(), name='create'),
    path('user/token/', views.CreateTokenView.as_view(), name='token'),
    path('user/me/', views.ManageUserView.as_view(), name='me'),

    path('', include(router.urls)),

    path('products/', views.ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view()),

    path('products_availability/', views.ProductAvailableListCreate.as_view()),
    path('products_availability/<int:pk>/', views.ProductAvailableDetail.as_view()),

]
