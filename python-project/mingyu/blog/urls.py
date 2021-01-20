from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',view.PostDetail.as_view()),
    path('',views.PostList.as_view()),
#    path('',views.index),
    
]