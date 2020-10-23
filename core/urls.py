"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include

from sahh import views, HodViews

urlpatterns = [
    path('demo/', views.show_demo_page),
    path('admin/', admin.site.urls),
    path('stuff/', include('stuff.urls')),
    path('', views.show_login_page),
    path('get_user_details', views.get_user_details),
    path('logout_user', views.logout_user),
    path('dologin',views.dologin),
    path('admin_home', HodViews.admin_home ),
    path('add_stuff', HodViews.add_stuff,name="add_stuff" ),
    path('add_stuff_save', HodViews.add_stuff_save, name="add_stuff_save"),
    path('manage_staff', HodViews.manage_staff, name="manage_staff"),
    path('edit_staff/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),
    path('delete_staff/<str:staff_id>', HodViews.delete_staff,name="delete_staff"),
    path('add_teacher', HodViews.add_teacher,name="add_teacher" ),
    path('add_teacher_save', HodViews.add_teacher_save, name="add_teacher_save"),
    path('manage_teacher', HodViews.manage_teacher, name="manage_teacher"),
    path('edit_teacher/<str:pk>/', HodViews.edit_teacher,name="edit_teacher"),
    path('edit_teacher_save', HodViews.edit_teacher_save,name="edit_teacher_save"),
    path('delete_teacher/<str:pk>', HodViews.delete_teacher,name="delete_teacher"),
    path('add_enterprise', HodViews.add_enterprise,name="add_enterprise" ),
    path('add_enterprise_save', HodViews.add_enterprise_save, name="add_enterprise_save"),
    path('manage_enterprise', HodViews.manage_enterprise, name="manage_enterprise"),
    path('edit_enterprise/<str:pk>/', HodViews.edit_enterprise,name="edit_enterprise"),
    path('edit_enterprise_save', HodViews.edit_enterprise_save,name="edit_enterprise_save"),
    path('delete_enterprise/<str:pk>', HodViews.delete_enterprise,name="delete_enterprise"),
    path('add_department', HodViews.add_department,name="add_department" ),
    path('add_department_save', HodViews.add_department_save, name="add_department_save"),
    path('manage_department', HodViews.manage_department, name="manage_department"),
    path('edit_department/<str:pk>/', HodViews.edit_department,name="edit_department"),
    path('edit_department_save', HodViews.edit_department_save,name="edit_department_save"),
    path('delete_department/<str:pk>', HodViews.delete_department,name="delete_department"),
    path('add_sections', HodViews.add_sections,name="add_sections" ),
    path('add_sections_save', HodViews.add_sections_save, name="add_sections_save"),
    path('manage_sections', HodViews.manage_sections, name="manage_sections"),
    path('edit_sections/<str:pk>/', HodViews.edit_sections,name="edit_sections"),
    path('edit_sections_save', HodViews.edit_sections_save,name="edit_sections_save"),
    path('delete_sections/<str:pk>', HodViews.delete_sections,name="delete_sections"),
    path('add_nursery', HodViews.add_nursery,name="add_nursery" ),
    path('add_nursery_save', HodViews.add_nursery_save, name="add_nursery_save"),
    path('manage_nursery', HodViews.manage_nursery, name="manage_nursery"),
    path('edit_nursery/<str:pk>/', HodViews.edit_nursery,name="edit_nursery"),
    path('edit_nursery_save', HodViews.edit_nursery_save,name="edit_nursery_save"),
    path('delete_nursery/<str:pk>', HodViews.delete_nursery,name="delete_nursery"),
    path('add_courses', HodViews.add_courses,name="add_courses" ),
    path('add_courses_save', HodViews.add_courses_save, name="add_courses_save"),
    path('manage_courses', HodViews.manage_courses, name="manage_courses"),
    path('edit_courses/<str:pk>/', HodViews.edit_courses,name="edit_courses"),
    path('edit_courses_save', HodViews.edit_courses_save,name="edit_courses_save"),
    path('delete_courses/<str:pk>', HodViews.delete_courses,name="delete_courses"),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
