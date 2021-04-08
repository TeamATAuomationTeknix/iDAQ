from django.urls import path
from bknd_iDAQ import views

urlpatterns =[
    path('unittable/',views.unit_table_API.as_view()),
    path('mstdevconn/',views.mst_dev_conn_API.as_view()),
    path('mstdevaddr/',views.mst_dev_addr_API.as_view()),
    path('shifttable/',views.shift_table_API.as_view()),
    path('userlevel/',views.user_level_API.as_view()),
    path('usermng/',views.user_mng_API.as_view()),

]
