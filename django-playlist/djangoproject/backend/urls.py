from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Subscriber', views.SubscriberView)
router1 = routers.DefaultRouter()
router1.register('Service', views.ServiceView)
router2 = routers.DefaultRouter()
router2.register('Organization', views.OrganizationView)

urlpatterns = [
    path('subscriber/', include(router.urls)),
    path('service/', include(router1.urls)),
    path('organization/', include(router2.urls)),
]
