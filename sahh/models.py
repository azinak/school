from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    user_type_data=((1,"HOD"),(2,"Staff"),(3,"Teacher"),(4,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):

    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Staffs(models.Model):

    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    phone=models.TextField(default='000000')
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    #profile_pic=models.FileField()
    #fcm_token=models.TextField(default="")
    objects=models.Manager()

class Students(models.Model):

    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    profile_pic=models.FileField()
    phone=models.TextField(default='000000')

    address=models.TextField()
    #course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    #session_year_id=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    #fcm_token=models.TextField(default="")
    objects = models.Manager()

class Teacher(models.Model):

    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    profile_pic=models.FileField()
    address=models.TextField()
    phone=models.TextField(default='000000')
    specialty= models.TextField(default="عام")
    #course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    #session_year_id=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    #fcm_token=models.TextField(default="")
    objects = models.Manager()

class Enterprise(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    note=models.TextField(default='لا يوجد')

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Nursery(models.Model): 
    
    name = models.CharField(max_length=255, unique=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, default=1)
    teme_choice = ((1,'صباحي'), (2, 'مسائي'))
    time = models.CharField(default=1, choices=teme_choice, max_length=10)
    price = models.FloatField(default=0.00, max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Courses(models.Model): 
    
    name = models.CharField(max_length=255, unique=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, default=1)
    price = models.FloatField(default=0.00, max_length=20)
    installment = models.IntegerField(default=4)
    shares = models.IntegerField(default=-1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Department(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    address=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Sections(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()



@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Staffs.objects.create(admin=instance,address="")
        if instance.user_type==3:
            Teacher.objects.create(admin=instance)
        if instance.user_type==4:
            Students.objects.create(admin=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staffs.save()
    if instance.user_type==3:
        instance.teacher.save()
    if instance.user_type==4:
        instance.students.save()