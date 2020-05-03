from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('details/<int:post_id>',views.post_details,name="detail"),
]
