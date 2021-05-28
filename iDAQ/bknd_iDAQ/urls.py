from django.urls import path
from bknd_iDAQ import views
from .views import RegisterAPI, LoginAPI
from knox import views as knox_views

urlpatterns =[
    path('unittable/',views.unit_table_API.as_view()),
    path('unittable/<int:pk>',views.unit_table_API.as_view()),
    path('mstdevconn/',views.mst_dev_conn_API.as_view()),
    path('mstdevconn/<int:pk>',views.mst_dev_conn_API.as_view()),
    path('mstdevaddr/',views.mst_dev_addr_API.as_view()),
    path('mstdevaddr/<int:pk>',views.mst_dev_addr_API.as_view()),
    path('mstdevaddr/<int:mst_dev_conn_id>',views.mst_dev_addr_API.as_view()),
    path('shifttable/',views.shift_table_API.as_view()),
    path('shifttable/<int:pk>',views.shift_table_API.as_view()),
    path('shifttable/<int:ShiftNumber>',views.shift_table_API.as_view()),
    path('userlevel/',views.user_level_API.as_view()),
    path('userlevel/<int:pk>',views.user_level_API.as_view()),
    path('usermng/',views.user_mng_API.as_view()),
    path('usermng/<int:pk>',views.user_mng_API.as_view()),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]
