from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


app_name = 'api'

router = DefaultRouter()
router.register('', views.StorageViewSet, basename='storages')
urlpatterns = router.urls

urlpatterns = [
    path('user/create/', views.CreateUserView.as_view(), name='create'),
    path('user/token/', views.CreateTokenView.as_view(), name='token'),
    path('user/me/', views.ManageUserView.as_view(), name='me'),

    path('category/<int:id>/', views.CategoryGenericAPIView.as_view()),
    path('category/', views.CategoryList.as_view()),

    path('products/', views.ProductsView.as_view()),
    path('products/<int:pk>/', views.SingleArticleView.as_view()),

    path('storages/', include(router.urls)),

]
