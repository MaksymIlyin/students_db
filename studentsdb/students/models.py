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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"