from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

# Create a router and register the UserViewSet
router = DefaultRouter()
router.register(r'users', views.ListUsersView, basename='user')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path("register/", views.CreateUserView.as_view(), name="register"),  #
    path("token/access/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    ]
