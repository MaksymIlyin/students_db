from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

from datetime import datetime

from .models import Student, Group

# Views for students
def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get("order_by", "")
    if order_by in ("last_name", "first_name", "ticket"):
        students = students.order_by(order_by)
        if request.GET.get("reverse", "") == "1":
            students = students.reverse()

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get("page")
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        # if page is out of range, deliver las page
        students = paginator.page(paginator.num_pages)
    return render(request, "students/students_list.html", {"students": students})


def students_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add botton clicked?
        if request.POST.get("add_button") is not None:

            # errors collection
            errors = {}
            # validate students data will go here
            data = {
                "middle_name": request.POST.get("middle_name"),
                "notes": request.POST.get("notes")
            }

            # validate user input
            first_name = request.POST.get("first_name", "").strip()
            if not first_name:
                errors["first_name"] = "First name required."
            else:
                data["first_name"] = first_name

            last_name = request.POST.get("last_name", "").strip()
            if not last_name:
                errors["last_name"] = "Last name required."
            else:
                data["last_name"] = last_name

            birthday = request.POST.get("birthday", "").strip()
            if not birthday:
                errors["birthday"] = "Birthday required."
            else:
                try:
                    datetime.strptime(birthday, "%Y-%m-%d")
                except Exception:
                    errors["birthday"] = "Incorrect date (exepmle: 1999-09-09)"
                else:
                    data["birthday"] = birthday

            ticket = request.POST.get("ticket", "").strip()
            if not ticket:
                errors["ticket"] = "Ticket required."
            else:
                data["ticket"] = ticket

            student_group = request.POST.get("student_group", "").strip()
            if not student_group:
                errors["student_group"] = "Student group required."
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors["student_group"] = "Choose a group."
                else:
                    data["student_group"] = groups[0]

            photo = request.FILES.get("photo")
            if photo:
                data["photo"] = photo

            if not errors:
                # create student object
                student = Student(**data)
                # save it to database
                student.save()

                # redirect user to students list
                return HttpResponseRedirect(
                    f"{reverse('home')}?status_message=Sudent Added!"
                    )
            else:
                # render form with errors and previos user input
                return render(
                    request, "students/students_add.html",
                    {"groups": Group.objects.all().order_by("title"),
                     "errors": errors}
                )
        elif request.POST.get("cancel_button") is not None:
            # redirect to homepage on cancel button
            return HttpResponseRedirect(
                f"{reverse('home')}?status_message=Student add cancelled!"
                )
    else:
        # initial form rende
        return render(request, "students/students_add.html",
                    {"groups": Group.objects.all().order_by("title")})


def students_edit(request, sid):
    return HttpResponse(f"<h1>Edit Student {sid}</h1>")


def students_delete(request, sid):
    return HttpResponse(f"<h1>Delete Students {sid}</h1>")


# Views for grouts
def groups_list(request):
    groups = [
        {"id": 1,
         "name": "?????? - 21",
         "head": "???????????? ??????????????"},
        {"id": 2,
         "name": "?????? - 22",
         "head": "???????????? ????????????"},
    ]
    return render(request, "students/groups_list.html", {"groups": groups})

def groups_add(request):
    return HttpResponse("<h1>Groups Add Form</h1>")

def groups_edit(request, gid):
    print(gid)
    return HttpResponse(f"<h1>Edit Groups {gid}</h1>")

def groups_delete(request, gid):
    return HttpResponse(f"<h1>Edit Groups {gid}</h1>")
