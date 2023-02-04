from django.urls import path

from StudentManagementApp2 import views

urlpatterns = [
    path('reg',views.reg_fun,name='register'),# it will redirect ot register.html page
    path("regdata",views.regdata_fun),#it will create superuser account
    path('',views.log_fun,name='log'),#it will redirect to login.html page
    path("logdata",views.logdata_fun),# it will read the data and verify
                                    # user is super user and redirect to home.html
    path('home',views.home_fun,name='home'),#it will redirect to home.html
    path('addstudents',views.add_fun,name='add'),#it will redirect to addstudent.html
    path("readdata",views.readdata_fun),#it will insert records into studenttable
    path('display',views.dis_fun,name='dis'),# it wll display student table data in display.html file
    path('update/<int:id>',views.update_fun,name='up'),#it will update the student details
    path('delete/<int:id>',views.delete_fun,name='del'),# it will delete the delete stydent etails
    path('log_out',views.log_out_fun,name='log_out'),#it will redirect to login page
]