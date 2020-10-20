from django.urls import path
from.import views
urlpatterns = [
    path('',views.Home,name="home"),
    path('load_form/',views.load_form,name="load_form"),
    path('/add/',views.add,name="add"),
    path('show/',views.show,name="show"),
]