from django.urls import path
from Admin_Panel import views

urlpatterns = [
    path('a_home/', views.a_home, name="a_home"),
    path('item/', views.item, name="item"),
    path('delete_item/<int:id>/', views.delete_item, name="delete_item"),

    path('display_booking/', views.display_booking, name="display_booking"),
    path('delete_booking/<int:id>/', views.delete_booking, name="delete_booking"),

    path('display_contact/', views.display_contact, name="display_contact"),
    path('delete_contact/<int:id>/', views.delete_contact, name="delete_contact"),


    path('display_user/', views.display_user, name="display_user"),

    path('save_asignup/', views.save_asignup, name="save_asignup"),
    path('a_sign_up/', views.a_sign_up, name="a_sign_up"),

    path('a_login/', views.a_login, name="a_login"),
    path('a_loged/', views.a_loged, name="a_loged"),

    path('a_logout/', views.a_logout, name="a_logout"),
    path('user_delete/<int:id>/', views.user_delete, name="user_delete"),
    path('edituser/<int:e>/', views.edituser, name="edituser"),
    path('updateuser/<int:u>/', views.updateuser, name="updateuser"),

    path('display_feedback/', views.display_feedback, name="display_feedback"),
    path('delete_feedback/<int:id>/', views.delete_feedback, name="delete_feedback"),

]