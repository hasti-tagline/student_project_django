from django.urls import path
from .api_views import StudentListCreateAPI, StudentRetrieveUpdateDeleteAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('students/', StudentListCreateAPI.as_view(), name='api_students'),
    path('students/<int:pk>/', StudentRetrieveUpdateDeleteAPI.as_view(), name='api_student_detail'),
]