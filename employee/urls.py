from django.urls import path
from . import views


urlpatterns = [
    path('empregister_view/',views.empregister_view,name='empregister'),

    path('emplogin_view/',views.emplogin_view,name='emplogin'),

    path('displayuser_view/',views.displayuser_view,name='displayuser'),


        path('displayadmin_view/',views.displayadmin_view,name='displayadmin'),





    # path('demo_view/',views.demo_view,name='demo'),
    # path('displaydata/',views.disp_userdata,name='dispuserdata'),
]
