from django.urls import path
from User_side import views

urlpatterns = [
    path('u_sign_up/', views.u_sign_up, name="u_sign_up"),
    path('save_usignup/', views.save_usignup, name="save_usignup"),
    path('u_login/', views.u_login, name="u_login"),
    path('u_loged/', views.u_loged, name="u_loged"),

    path('u_home/', views.u_home, name="u_home"),

    path('u_contact/', views.u_contact, name="u_contact"),
    path('savecontact/', views.savecontact, name="savecontact"),

    path('register/', views.register, name="register"),
    path('saveregistration/', views.saveregistration, name="saveregistration"),

    path('about/', views.about, name="about"),
    path('all_band/', views.all_band, name="all_band"),

    path('single_page/<int:bandid>/', views.single_page, name="single_page"),
    path('feedback/', views.feedback, name="feedback"),


    path('music', views.music, name="music"),
    path('test', views.test, name="test"),
    path('filter/<cat>/', views.filter, name="filter"),
    path('booking/', views.booking, name="booking"),
]