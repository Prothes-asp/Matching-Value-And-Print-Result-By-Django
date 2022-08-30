from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name="home"),
    path('link/',views.link,name="link"),
    path('action/',views.action,name="action"),
]
