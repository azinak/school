from django.db import models
from sahh.models import Courses, CustomUser, Department, Enterprise, Nursery, Sections, Staffs, Students, Teacher
 
class Batch(models.Model): 
    
    name = models.CharField(max_length=255, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, default=1)
    state_choice = ((1,'مسودة'),(2,'نشطة'),(3,'مغلقة'))
    state = models.CharField(default=1, choices=state_choice, max_length=10)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()



class Cohort(models.Model): 
    
    
    student = models.ForeignKey(Students, on_delete=models.CASCADE, default=1)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, default=1)
    

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()