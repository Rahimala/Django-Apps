from django.urls import path
from apps import views

urlpatterns = [
    #path('student/<my_id>/', views.show, name="detail"),
    path('student/<int:my_id>/', views.show, name="detail"),
    path('student/<int:my_id>/<int:my_subid>/', views.show_subdetail, name="subdetail"),
    path('', views.home,{'check':'Ok'}, name='home')

  ]
# path('home/index/=/*^/', views.app)
# http://127.0.0.1:8000/home/index/=/*%5E/
