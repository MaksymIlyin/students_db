# -*- coding: utf-8 -*-
from django.db import models

class Student(models.Model):
    """Student model"""

    class Meta():
        verbose_name = "Student"
        verbose_name_plural = "Students"

    first_name = models.CharField(
        max_length=265,
        blank=False,
        verbose_name="Name"
    )

    last_name = models.CharField(
        max_length=265,
        blank=False,
        verbose_name="Last name"
    )

    middle_name = models.CharField(
        max_length=265,
        blank=True,
        verbose_name="Middle name",
        default=""
    )

    birthday = models.DateField(
        max_length=265,
        blank=True,
        verbose_name="Birth day",
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name="Photo",
        null=True
    )

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Ticket"
    )

    notes = models.TextField(
        blank=True,
        verbose_name="Additional notes"
    )

    student_group = models.ForeignKey(
        "Group",
        verbose_name="Group",
        blank=False,
        null=True,
        on_delete=models.PROTECT
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    """Group Model"""

    class Meta():
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Title"
    )

    leader = models.OneToOneField(
        "Student",
        verbose_name="Leader",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
        )

    notes = models.TextField(
        blank=True,
        verbose_name="Additional Notes"
    )

    def __str__(self):
        if self.leader:
            return f"{self.title} - leader {self.leader.first_name} {self.leader.last_name}"
        else:
            return f"{self.title}"