from django.contrib import admin
from .models import Subscriber, UserInfo, SubscriptionType, Service, Organization

admin.site.register(Subscriber)
admin.site.register(Service)
admin.site.register(Organization)
