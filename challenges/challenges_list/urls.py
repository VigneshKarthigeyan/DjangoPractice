from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="challenges"),
    path("<int:month>/",views.monthly_challenges_by_number),
    path("<str:month>/",views.monthly_challenges,name="monthly_challenges"),
    # path('january/', views.jan),
    # path('february/',views.feb)
]