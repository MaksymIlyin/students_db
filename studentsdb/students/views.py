from django.shortcuts import render
from django.http import HttpResponse

# Views for students
def students_list(request):
    students = [
        {"id": 1,
        "first_name": "Віталій",
        "last_name": "Подоба",
        "ticket": 123,
        "image": "img/student_1.jpg"},
        {"id": 2,
        "first_name": "Андрій",
        "last_name": "Корост",
        "ticket": 343,
        "image": "img/student_2.jpg"}
    ]
    return render(request, "students/students_list.html", {"students": students})

def students_add(request):
    return HttpResponse("<h1>Students Add Form</h1>")

def students_edit(request, sid):
    return HttpResponse(f"<h1>Edit Student {sid}</h1>")

def students_delete(request, sid):
    return HttpResponse(f"<h1>Delete Students {sid}</h1>")

# Views for grouts
def groups_list(request):
    print("Groups list part")
    return HttpResponse(request, "<h1>Groups Listing</h1>")

def groups_add(request):
    return HttpResponse("<h1>Groups Add Form</h1>")

def groups_edit(request, gid):
    print(gid)
    return HttpResponse(f"<h1>Edit Groups {gid}</h1>")

def groups_delete(request, gid):
    return HttpResponse(f"<h1>Edit Groups {gid}</h1>")
