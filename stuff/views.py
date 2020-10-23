from django.shortcuts import render

from sahh.models import Courses, CustomUser, Department, Enterprise, Nursery, Sections, Staffs, Students, Teacher

def show_demo_page(request):
    return render(request, 'stuff_template/index.html')