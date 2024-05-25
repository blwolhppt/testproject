from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api import views

router = SimpleRouter()

router.register('organizations', views.OrganizationsViewSet)
router.register('shops', views.ShopsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
