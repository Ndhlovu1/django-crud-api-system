from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('edit-menu/<int:pk>', views.SingleItemView.as_view())
]





