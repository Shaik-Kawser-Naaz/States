from django.urls import path
from AP import views
urlpatterns=[
    path('fest1',views.wish1),
    path('fest2',views.wish2),
    path('fest3',views.wish3),
]