from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/login/',
         auth_views.LoginView.as_view(template_name='login.html')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

]
