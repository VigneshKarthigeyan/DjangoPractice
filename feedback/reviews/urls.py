from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view()),
    path('reviews', ReviewsListView.as_view()),
    path('reviews/<int:id>', ReviewView.as_view(),name="singlereview"),
]
