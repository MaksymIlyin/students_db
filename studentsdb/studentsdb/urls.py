"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
import students.views

from .settings import MEDIA_ROOT, MEDIA_URL, DEBUG

urlpatterns = [
    path("", students.views.students_list, name="home"),
    path("students/add", students.views.students_add, name="students_add"),
    path("students/<int:sid>/edit", students.views.students_edit, name="students_edit"),
    path("students/<int:sid>/delete", students.views.students_delete, name="students_delete"),

    path("groups/", students.views.groups_list, name="groups"),
    path("groups/add", students.views.groups_add, name="groups_add"),
    path("groups/<int:gid>/edit", students.views.groups_edit, name="groups_edit"),
    path("groups/<int:gid>/delete", students.views.groups_delete, name="groups_delete"),

    path('admin/', admin.site.urls),
]

if DEBUG:
    # serve files from media folder
    urlpatterns += static(
        MEDIA_URL,
        document_root=MEDIA_ROOT)