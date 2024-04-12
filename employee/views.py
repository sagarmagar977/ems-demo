from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import *
from django.db.models import Q
from django.contrib import messages


def home(request):
    return render(request,"home.html")

def view_emp(request):
    all_emp=employee.objects.all()
    context={"all_emp":all_emp}
    return render(request,"view_emp.html",context)

def add_emp(request):
    if request.method=="POST":
       
        name=request.POST['name']
        role=int(request.POST['role'])
        department=int(request.POST['department'])
        salary=int(request.POST['salary']) 
        hire_date=request.POST['hire_date']
        new_emp=employee(name=name,role_id=role,department_id=department,salary=salary,hire_date=hire_date)
        new_emp.save()
        messages.success(request,"employee added succesfully")
        return render(request,"add_emp.html")
        
        
        
    else:
        print("get")
        return render(request,'add_emp.html')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            remove_emp_id=employee.objects.get(id=emp_id)
            remove_emp_id.delete()
            messages.success(request,"employee removed succesfully")
            
        except:
            messages.error(request,"unexpected error ")
            
            
    emp=employee.objects.all()
    context={"emp":emp}
    return render(request,"remove_emp.html",context)


def update_emp(request,emp_id=0):
    if emp_id:
        try:
            update_emp_id=employee.objects.get(id=emp_id)
            update_emp_id.save()
            return HttpResponse("employee deleted! ")
        except:
            return HttpResponse("invalid try")
            
    emp=employee.objects.all()
    context={"emp":emp}
    return render(request,"remove_emp.html",context)








def search_emp(request):
    if request.method == "POST":  
        name = request.POST.get('name')
        role = request.POST.get('role')
        department = request.POST.get('department')
        emps = employee.objects.all()

        if name:
            all_emps = emps.filter(name__icontains=name)
        if department:
            all_emps = emps.filter(department__name=department)
        if role:
            all_emps = emps.filter(role__name=role)

        context = {
            "all_emp": all_emps
        }
        return render(request, 'view_emp.html', context)
    elif request.method == "GET":
        return render(request, "search_emp.html")  # Changed template name here
    else:
        return HttpResponse("Unexpected error occurred!")

            
    
      


