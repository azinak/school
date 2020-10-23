from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import CustomUser, Staffs, Students, Teacher, Enterprise, Department, Sections, Courses,Nursery
from django.urls import reverse

# Create your views here.
def admin_home(request):
    return render(request, 'hub_template/index.html')
   
def add_stuff(request):
    return render(request, 'hub_template/add_stuff.html')

def add_stuff_save(request):
    
    if request.method != "POST":
        return HttpResponse("<h2>Methon Not allowd</h2>")
    else :

        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        passwrod = request.POST.get('passwrod')

        try :
            #user, created = CustomUser.objects.get_or_create(first_name=first_name, last_name=last_name, defaults={'username':username, 'password':passwrod, 'user_type':2})
            #if created==False :
            #    user.stuff.address = address
            #    user.stuff.phone = phone
            #    user.save()
            #    print('aziz')
            #    messages.success(request,"تم إضافة الموظف بنجاح")
            user = CustomUser.objects.get(first_name=first_name, last_name=last_name)
            print('found')
            messages.info(request, 'الموظف موجود')
            return HttpResponseRedirect(reverse("add_stuff"))
        except CustomUser.DoesNotExist :
            user = CustomUser.objects.create(first_name=first_name, last_name=last_name, username=username, password=passwrod, user_type=2)
            user.staffs.address = address
            user.staffs.phone = phone
            user.save()
            messages.success(request,"تم إضافة الموظف بنجاح")
            return HttpResponseRedirect(reverse("add_stuff"))

        except :
            messages.error(request,"فشل في إضافة موظف")
            print('nothing')
            return HttpResponseRedirect(reverse("add_stuff"))


def manage_staff(request):
    
    staffs=Staffs.objects.all()
    return render(request,"hub_template/manage_staff.html",{"staffs":staffs})

def edit_staff(request, staff_id):
    
    staff=Staffs.objects.get(admin=staff_id)
    return render(request,"hub_template/edit_staff.html",{"staff":staff,"id":staff_id})

def edit_staff_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        passwrod = request.POST.get('passwrod')

        try :
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.password = passwrod
            user.save()

            staff = Staffs.objects.get(admin=staff_id)
            staff.address = address
            staff.phone = phone
            staff.save()
            messages.success(request,"تم التعديل بنجاح")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))


def delete_staff(request, staff_id):
    
    user = CustomUser.objects.get(id=staff_id)
    user.delete()
    return HttpResponseRedirect(reverse("manage_staff"))


def add_teacher(request):
    return render(request, 'hub_template/add_teacher.html')

def add_teacher_save(request):
    
    if request.method != "POST":
        return HttpResponse("<h2>Methon Not allowd</h2>")
    else :

        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        specialty = request.POST.get('specialty')
        email = request.POST.get('email')
        #last_name = request.POST.get('lname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        passwrod = request.POST.get('passwrod')

        try :
            #user, created = CustomUser.objects.get_or_create(first_name=first_name, last_name=last_name, defaults={'username':username, 'password':passwrod, 'user_type':2})
            #if created==False :
            #    user.stuff.address = address
            #    user.stuff.phone = phone
            #    user.save()
            #    print('aziz')
            #    messages.success(request,"تم إضافة الموظف بنجاح")
            user = CustomUser.objects.get(first_name=first_name, last_name=last_name)
            print('found')
            messages.info(request, 'الأستاذ موجود')
            return HttpResponseRedirect(reverse("add_teacher"))
        except CustomUser.DoesNotExist :
            user = CustomUser.objects.create(first_name=first_name, last_name=last_name, username=username, password=passwrod,email=email, user_type=3)
            user.teacher.address = address
            user.teacher.phone = phone
            user.teacher.specialty = specialty
            user.save()
            messages.success(request,"تم إضافة الأستاذ بنجاح")
            return HttpResponseRedirect(reverse("add_teacher"))

        except :
            messages.error(request,"فشل في إضافة الأستاذ")
            print('nothing')
            return HttpResponseRedirect(reverse("add_teacher"))


def manage_teacher(request):
    
    teachers=Teacher.objects.all()
    return render(request,"hub_template/manage_teacher.html",{"teachers":teachers})

def edit_teacher(request, pk):
    
    teacher=Teacher.objects.get(admin=pk)
    return render(request,"hub_template/edit_teacher.html",{"teacher":teacher})

def edit_teacher_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        teacher_id = request.POST.get('teacher_id')
        print(teacher_id)
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        specialty = request.POST.get('specialty')
        email = request.POST.get('email')
        print(email)
        #last_name = request.POST.get('lname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        passwrod = request.POST.get('passwrod')
        


        try :
            user = CustomUser.objects.get(id=teacher_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.password = passwrod
            user.save()

            staff = Teacher.objects.get(admin=teacher_id)
            staff.address = address
            staff.phone = phone
            staff.specialty = specialty
            staff.save()
            messages.success(request,"تم التعديل بنجاح")
            return HttpResponseRedirect(reverse("edit_teacher",kwargs={"pk":teacher_id}))
        except:
            messages.error(request,"فشل النظام في تعديل معلومات الأستاذ")
            return HttpResponseRedirect(reverse("edit_teacher",kwargs={"pk":teacher_id}))
        
        


def delete_teacher(request, pk):
    
    user = CustomUser.objects.get(id=pk)
    user.delete()
    return HttpResponseRedirect(reverse("manage_teacher"))


def add_enterprise(request):
    return render(request, 'hub_template/add_enterprise.html')

def add_enterprise_save(request):
    
    if request.method != "POST":
        return HttpResponse("<h2>Methon Not allowd</h2>")
    else :

        name = request.POST.get('name')
        note = request.POST.get('note')
        

        try :
            #user, created = CustomUser.objects.get_or_create(first_name=first_name, last_name=last_name, defaults={'username':username, 'password':passwrod, 'user_type':2})
            #if created==False :
            #    user.stuff.address = address
            #    user.stuff.phone = phone
            #    user.save()
            #    print('aziz')
            #    messages.success(request,"تم إضافة الموظف بنجاح")
            user = Enterprise.objects.get(name=name)
            print('found')
            messages.info(request, 'المؤسسة موجودة')
            return HttpResponseRedirect(reverse("add_enterprise"))
        except Enterprise.DoesNotExist :
            user = Enterprise.objects.create(name=name, note=note)
            user.save()
            messages.success(request,"تم إضافة المؤسسة بنجاح")
            return HttpResponseRedirect(reverse("add_enterprise"))

        except :
            messages.error(request,"فشل في إضافة المؤسسة")
            print('nothing')
            return HttpResponseRedirect(reverse("add_enterprise"))


def manage_enterprise(request):
    
    objs=Enterprise.objects.all()
    return render(request,"hub_template/manage_enterprise.html",{"objs":objs})

def edit_enterprise(request, pk):
    
    obj=Enterprise.objects.get(id=pk)
    return render(request,"hub_template/edit_enterprise.html",{"obj":obj})

def edit_enterprise_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        pk = request.POST.get('id')
        name = request.POST.get('name')
        note = request.POST.get('note')
        
        print(pk)


        try :
            user = Enterprise.objects.get(id=pk)
            user.name = name
            user.note = note
            
            user.save()

            
            messages.success(request,"تم التعديل بنجاح")
            return HttpResponseRedirect(reverse("edit_enterprise",kwargs={"pk":pk}))
        except:
            messages.error(request,"فشل النظام في تعديل معلومات المؤسسة")
            return HttpResponseRedirect(reverse("edit_enterprise",kwargs={"pk":pk}))
        
        


def delete_enterprise(request, pk):
    
    user = Enterprise.objects.get(id=pk)
    user.delete()
    return HttpResponseRedirect(reverse("manage_enterprise"))


def add_department(request):
    return render(request, 'hub_template/add_department.html')

def add_department_save(request):
    
    if request.method != "POST":
        return HttpResponse("<h2>Methon Not allowd</h2>")
    else :

        name = request.POST.get('name')
        address = request.POST.get('address')
        

        try :
            #user, created = CustomUser.objects.get_or_create(first_name=first_name, last_name=last_name, defaults={'username':username, 'password':passwrod, 'user_type':2})
            #if created==False :
            #    user.stuff.address = address
            #    user.stuff.phone = phone
            #    user.save()
            #    print('aziz')
            #    messages.success(request,"تم إضافة الموظف بنجاح")
            user = Department.objects.get(name=name)
            print('found')
            messages.info(request, 'المقر موجود')
            return HttpResponseRedirect(reverse("add_department"))
        except Department.DoesNotExist :
            user = Department.objects.create(name=name, address=address)
            user.save()
            messages.success(request,"تم إضافة المقر بنجاح")
            return HttpResponseRedirect(reverse("add_department"))

        except :
            messages.error(request,"فشل في إضافة المقر")
            print('nothing')
            return HttpResponseRedirect(reverse("add_department"))


def manage_department(request):
    
    objs=Department.objects.all()
    return render(request,"hub_template/manage_department.html",{"objs":objs})

def edit_department(request, pk):
    
    obj=Department.objects.get(id=pk)
    return render(request,"hub_template/edit_department.html",{"obj":obj})

def edit_department_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        pk = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        
        print(pk)


        try :
            user = Department.objects.get(id=pk)
            user.name = name
            user.address = address
            
            user.save()

            
            messages.success(request,"تم التعديل بنجاح")
            return HttpResponseRedirect(reverse("edit_department",kwargs={"pk":pk}))
        except:
            messages.error(request,"فشل النظام في تعديل معلومات المؤسسة")
            return HttpResponseRedirect(reverse("edit_department",kwargs={"pk":pk}))
        
        


def delete_department(request, pk):
    
    user = Department.objects.get(id=pk)
    print(user)
    user.delete()
    return HttpResponseRedirect(reverse("manage_department"))


def add_sections(request):
    deps = Department.objects.all()
    return render(request, 'hub_template/add_sections.html', {"deps":deps})

def add_sections_save(request):
    
    if request.method != "POST":
        return HttpResponse("<h2>Methon Not allowd</h2>")
    else :

        name = request.POST.get('name')
        dep = request.POST.get('department')
        department = Department.objects.get(id=dep)
    

        try :
            #user, created = CustomUser.objects.get_or_create(first_name=first_name, last_name=last_name, defaults={'username':username, 'password':passwrod, 'user_type':2})
            #if created==False :
            #    user.stuff.address = address
            #    user.stuff.phone = phone
            #    user.save()
            #    print('aziz')
            #    messages.success(request,"تم إضافة الموظف بنجاح")
            user = Sections.objects.get(name=name)
            print('found')
            messages.info(request, 'القسم موجود')
            return HttpResponseRedirect(reverse("add_sections"))
        except Sections.DoesNotExist :
            user = Sections.objects.create(name=name, department=department)
            user.save()
            messages.success(request,"تم إضافة القسم بنجاح")
            return HttpResponseRedirect(reverse("add_sections"))

        except :
            messages.error(request,"فشل في إضافة القسم")
            print('nothing')
            return HttpResponseRedirect(reverse("add_sections"))


def manage_sections(request):
    
    objs=Sections.objects.all()
    return render(request,"hub_template/manage_sections.html",{"objs":objs})

def edit_sections(request, pk):
    deps = Department.objects.all()
    obj=Sections.objects.get(id=pk)
    return render(request,"hub_template/edit_sections.html",{"obj":obj, "deps":deps})

def edit_sections_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        pk = request.POST.get('id')
        name = request.POST.get('name')
        dep = request.POST.get('department')
        department = Department.objects.get(id=dep)
        
        print(pk)


        try :
            user = Sections.objects.get(id=pk)
            user.name = name
            user.department = department
            
            user.save()

            
            messages.success(request,"تم التعديل بنجاح")
            return HttpResponseRedirect(reverse("edit_sections",kwargs={"pk":pk}))
        except:
            messages.error(request,"فشل النظام في تعديل معلومات المؤسسة")
            return HttpResponseRedirect(reverse("edit_sections",kwargs={"pk":pk}))
        
        


def delete_sections(request, pk):
    
    user = Sections.objects.get(id=pk)
    print(user)
    user.delete()
    return HttpResponseRedirect(reverse("manage_sections"))

def add_nursery(request):
    deps = Enterprise.objects.all()
    return render(request, 'hub_template/add_nursery.html', {"deps":deps})

def add_nursery_save(request):
    
    if request.method != "POST":
        return HttpResponse("<h2>Methon Not allowd</h2>")
    else :

        name = request.POST.get('name')
        time = request.POST.get('time')
        price = request.POST.get('price')
        dep = request.POST.get('enterprise')
        enterprise = Enterprise.objects.get(id=dep)
    

        try :
            #user, created = CustomUser.objects.get_or_create(first_name=first_name, last_name=last_name, defaults={'username':username, 'password':passwrod, 'user_type':2})
            #if created==False :
            #    user.stuff.address = address
            #    user.stuff.phone = phone
            #    user.save()
            #    print('aziz')
            #    messages.success(request,"تم إضافة الموظف بنجاح")
            user = Nursery.objects.get(name=name)
            print('found')
            messages.info(request, 'القسم موجود')
            return HttpResponseRedirect(reverse("add_nursery"))
        except Nursery.DoesNotExist :
            user = Nursery.objects.create(name=name,time=time,price=price, enterprise=enterprise)
            user.save()
            messages.success(request,"تم إضافة القسم بنجاح")
            return HttpResponseRedirect(reverse("add_nursery"))

        except :
            messages.error(request,"فشل في إضافة القسم")
            print('nothing')
            return HttpResponseRedirect(reverse("add_nursery"))


def manage_nursery(request):
    
    objs=Nursery.objects.all()
    return render(request,"hub_template/manage_nursery.html",{"objs":objs})

def edit_nursery(request, pk):
    deps = Enterprise.objects.all()
    obj=Nursery.objects.get(id=pk)
    return render(request,"hub_template/edit_nursery.html",{"obj":obj, "deps":deps})

def edit_nursery_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        pk = request.POST.get('id')
        name = request.POST.get('name')
        time = request.POST.get('time')
        price = request.POST.get('price')
        dep = request.POST.get('enterprise')
        enterprise = Enterprise.objects.get(id=dep)
        
        print(pk)


        try :
            user = Nursery.objects.get(id=pk)
            user.name = name
            user.time = time
            user.price = price
            user.enterprise = enterprise
            
            user.save()

            
            messages.success(request,"تم التعديل بنجاح")
            return HttpResponseRedirect(reverse("edit_nursery",kwargs={"pk":pk}))
        except:
            messages.error(request,"فشل النظام في تعديل معلومات المؤسسة")
            return HttpResponseRedirect(reverse("edit_nursery",kwargs={"pk":pk}))
        
        


def delete_nursery(request, pk):
    
    user = Nursery.objects.get(id=pk)
    print(user)
    user.delete()
    return HttpResponseRedirect(reverse("manage_nursery"))

def add_courses(request):
    deps = Enterprise.objects.all()
    return render(request, 'hub_template/add_courses.html', {"deps":deps})

def add_courses_save(request):
    
    if request.method != "POST":
        return HttpResponse("<h2>Methon Not allowd</h2>")
    else :

        name = request.POST.get('name')
        installment = request.POST.get('installment')
        shares = request.POST.get('shares')
        price = request.POST.get('price')
        dep = request.POST.get('enterprise')
        enterprise = Enterprise.objects.get(id=dep)
    

        try :
            #user, created = CustomUser.objects.get_or_create(first_name=first_name, last_name=last_name, defaults={'username':username, 'password':passwrod, 'user_type':2})
            #if created==False :
            #    user.stuff.address = address
            #    user.stuff.phone = phone
            #    user.save()
            #    print('aziz')
            #    messages.success(request,"تم إضافة الموظف بنجاح")
            user = Courses.objects.get(name=name)
            print('found')
            messages.info(request, 'الدورة موجودة')
            return HttpResponseRedirect(reverse("add_courses"))
        except Courses.DoesNotExist :
            user = Courses.objects.create(name=name,installment=installment, shares=shares,price=price, enterprise=enterprise)
            user.save()
            messages.success(request,"تم إضافة الدورة بنجاح")
            return HttpResponseRedirect(reverse("edit_courses",kwargs={"pk":user.id}))

        except :
            messages.error(request,"فشل في إضافة الدورة")
            print('nothing')
            return HttpResponseRedirect(reverse("add_courses"))


def manage_courses(request):
    
    objs=Courses.objects.all()
    return render(request,"hub_template/manage_courses.html",{"objs":objs})

def edit_courses(request, pk):
    deps = Enterprise.objects.all()
    obj=Courses.objects.get(id=pk)
    return render(request,"hub_template/edit_courses.html",{"obj":obj, "deps":deps})

def edit_courses_save(request):
    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        pk = request.POST.get('id')
        name = request.POST.get('name')
        installment = request.POST.get('installment')
        shares = request.POST.get('shares')
        price = request.POST.get('price')
        dep = request.POST.get('enterprise')
        enterprise = Enterprise.objects.get(id=dep)
        
        print(pk)


        try :
            user = Courses.objects.get(id=pk)
            user.name = name
            user.installment = installment
            user.shares = shares
            user.price = price
            user.enterprise = enterprise
            
            user.save()

            
            messages.success(request,"تم التعديل بنجاح")
            return HttpResponseRedirect(reverse("edit_courses",kwargs={"pk":pk}))
        except:
            messages.error(request,"فشل النظام في تعديل معلومات الدورة")
            return HttpResponseRedirect(reverse("edit_courses",kwargs={"pk":pk}))
        
        


def delete_courses(request, pk):
    
    user = Nursery.objects.get(id=pk)
    print(user)
    user.delete()
    return HttpResponseRedirect(reverse("manage_courses"))

