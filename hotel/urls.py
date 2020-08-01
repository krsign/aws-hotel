from django.urls import path
from .views import HomeView, customer_detail_form, About, CategoryList

urlpatterns = [
    path('category/<int:id>', CategoryList.as_view(), name='filter'),
    path('', HomeView.as_view(), name='home'),
    path('detail', customer_detail_form, name='detail'),
    path('aboutpage', About.as_view(), name='about'),
  
]
