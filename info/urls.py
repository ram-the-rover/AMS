from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),

    path('teacher/<slug:teacher_id>/Classes/',
         views.t_clas, name='t_clas'),
    
    path('teacher/<int:assign_id>/Students/attendance/',
         views.t_student, name='t_student'),

   
    path('teacher/<int:assign_id>/Extra_class/',
         views.t_extra_class, name='t_extra_class'),
    path('teacher/<slug:assign_id>/Extra_class/confirm/',
         views.e_confirm, name='e_confirm'),

]
admin.site.site_url = 'admin'
admin.site.site_header = 'My Site'
