from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp


def emp_home(request):
    try:
        emps = Emp.objects.all()
        return render(request, "emp/home.html", {'emps': emps})
    except Exception as e:
        return render(request, "error.html", {'error_message': str(e)})


def add_emp(request):
    if request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get('last_name')
            emp_id = request.POST.get("emp_id")
            email = request.POST.get("email")
            emp_phone = request.POST.get("emp_phone")
            emp_address = request.POST.get("emp_address")
            emp_working = request.POST.get("emp_working")
            emp_department = request.POST.get("emp_department")

            e = Emp()
            e.first_name = first_name
            e.last_name = last_name
            e.emp_id = emp_id
            e.email = email
            e.phone = emp_phone
            e.address = emp_address
            e.department = emp_department
            e.working = bool(emp_working)

            e.save()
            return redirect("/emp/home/")
        except Exception as e:
            return render(request, "error.html", {'error_message': str(e)})
    return render(request, "emp/add_emp.html", {})

def delete_emp(request, emp_id):
    try:
        emp = Emp.objects.get(pk=emp_id)
        emp.delete()
        return redirect("/emp/home/")
    except Emp.DoesNotExist:
        return render(request, "error.html", {'error_message': f"Employee with ID {emp_id} not found."})
    except Exception as e:
        return render(request, "error.html", {'error_message': str(e)})

def update_emp(request, emp_id):
    try:
        emp = Emp.objects.get(pk=emp_id)
        return render(request, "emp/update_emp.html", {
            'emp': emp
        })
    except Emp.DoesNotExist:
        return render(request, "error.html", {'error_message': f"Employee with ID {emp_id} not found."})
    except Exception as e:
        return render(request, "error.html", {'error_message': str(e)})

def do_update_emp(request, emp_id):
    if request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get('last_name')
            emp_id_temp = request.POST.get("emp_id")
            emp_email = request.POST.get("emp_email")
            emp_phone = request.POST.get("emp_phone")
            emp_address = request.POST.get("emp_address")
            emp_working = request.POST.get("emp_working")
            emp_department = request.POST.get("emp_department")

            e = Emp.objects.get(pk=emp_id)

            e.first_name = first_name
            e.last_name = last_name
            e.emp_id = emp_id_temp
            e.email = emp_email
            e.phone = emp_phone
            e.address = emp_address
            e.department = emp_department
            e.working = bool(emp_working)  

            e.save()
            return redirect("/emp/home/")
        except Emp.DoesNotExist:
            return render(request, "error.html", {'error_message': f"Employee with ID {emp_id} not found."})
        except Exception as e:
            return render(request, "error.html", {'error_message': str(e)})

    return redirect("/emp/home/")

