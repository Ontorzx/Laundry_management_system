from django.urls import path
from.import views

urlpatterns = [
    path('',views.add_show,name="add_show"),
    path('add/',views.add,name="add"),
    path('delete/<int:id>/',views.delete_data,name="delete_data"),
    path('update/<int:id>/',views.update_data,name="update_data"),
]