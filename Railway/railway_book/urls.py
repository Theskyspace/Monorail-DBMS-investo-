from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('choice',views.choice),
    path('recent/',views.recent),
    path('recent/delete/',views.delete)
]
