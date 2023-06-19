from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ReviewListView.as_view(), name='review-list'),
    path('add/', ReviewCreateView.as_view(), name='review-create'),
]