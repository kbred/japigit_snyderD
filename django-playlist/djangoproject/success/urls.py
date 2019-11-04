from django.urls import path
from . import views

app_name = 'success'

urlpatterns = [
    path('confirm/', views.confirm_view, name="confirm")
]
