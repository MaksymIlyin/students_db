from django.shortcuts import render
from django.http import HttpResponse

from .models import Student

# Views for students
def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get("order_by", "")
    if order_by in ("last_name", "first_name", "ticket"):
        students = students.order_by(order_by)
        if request.GET.get("reverse", "") == "1":
            students = students.reverse()
    return render(request, "students/students_list.html", {"students": students})

def students_add(request):
    return HttpResponse("<h1>Students Add Form</h1>")

def students_edit(request, sid):
    return HttpResponse(f"<h1>Edit Student {sid}</h1>")

def students_delete(request, sid):
    return HttpResponse(f"<h1>Delete Students {sid}</h1>")

# Views for grouts
def groups_list(request):
    groups = [
        {"id": 1,
         "name": "МтМ - 21",
         "head": "Подоба Віталій"},
        {"id": 2,
         "name": "МтМ - 22",
         "head": "Корост Андрій"},
    ]
    return render(request, "students/groups_list.html", {"groups": groups})

def groups_add(request):
    return HttpResponse("<h1>Groups Add Form</h1>")

def groups_edit(request, gid):
    print(gid)
    return HttpResponse(f"<h1>Edit Groups {gid}</h1>")

def groups_delete(request, gid):
    return HttpResponse(f"<h1>Edit Groups {gid}</h1>")
