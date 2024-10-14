from django.urls import path
from . import views



urlpatterns = [
  path("user-detail/<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),
  path("user-update/<int:pk>/", views.UserUpdateView.as_view(), name="user_update"),
]