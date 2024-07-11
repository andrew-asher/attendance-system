from django.contrib import admin
from django.urls import path, include
from authentication.views import LoginView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/auth/login/', LoginView.as_view(), name='login'),
]
