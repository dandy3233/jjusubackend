from django.urls import path
from .views import StaffListView, ImageCollageListView

urlpatterns = [
    path('staff/', StaffListView.as_view(), name='staff-list'),
    path('image-collage/', ImageCollageListView.as_view(), name='image-collage-list'),
]
