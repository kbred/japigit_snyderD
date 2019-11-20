from django.shortcuts import render
from rest_framework import viewsets
from .models import Subscriber, Service, Organization
from .serializers import SubscriberSerializer, ServiceSerializer, OrganizationSerializer

class SubscriberView(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class OrganizationView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
