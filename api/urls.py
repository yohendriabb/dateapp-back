from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from .views import CreateUserview, SpecialtiesListCreate, SpecialtiesDelete

urlpatterns = [
    path('user/register/', CreateUserview.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='get_refresh'),
    path('-auth/', TokenObtainPairView.as_view(), name='get_token'),

    path('specialties/', SpecialtiesListCreate.as_view(), name='specialties'),
    path('specialties-delete/', SpecialtiesDelete.as_view(), name='special-delete')
]