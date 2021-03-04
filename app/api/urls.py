from django.urls import path

from . import views


app_name = 'api'

urlpatterns = [
    path('user/create/', views.CreateUserView.as_view(), name='create'),
    path('user/token/', views.CreateTokenView.as_view(), name='token'),
    path('user/me/', views.ManageUserView.as_view(), name='me'),
]
