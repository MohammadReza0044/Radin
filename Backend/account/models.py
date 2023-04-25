from django.contrib.auth.models import AbstractUser
from django.db import models
from extensions.utils import jalali_converter


class User(AbstractUser):
    personal_number = models.IntegerField(null=True)
    national_code = models.IntegerField(null=True)
    birthday_date = models.DateField(null=True)
    phone_number = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    job_position = models.CharField(max_length=255, null=True)
    job_description = models.CharField(max_length=255, null=True)
    is_Employee = models.BooleanField(default=True, null=True)
    is_Administration_Manager = models.BooleanField(default=False, null=True)
    is_CEO = models.BooleanField(default=False, null=True)
    picture = models.ImageField(upload_to="users/image", null=True)

    class Meta:
        db_table = "User"

    def jalali_date(self):
        return jalali_converter(self.birthday_date)


class Vacation(models.Model):
    VACATION_TYPE_CHOICES = (
        ("Daily", "مرخصی روزانه"),
        ("Hourly", "مرخصی ساعتی"),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vacation_type = models.CharField(max_length=50, choices=VACATION_TYPE_CHOICES)
    date = models.DateField()
    from_hour = models.TimeField(null=True)
    untill_hour = models.TimeField(null=True)
    description = models.TextField()
    is_accept = models.BooleanField(default=False)

    class Meta:
        db_table = "Vacation"

    def jalali_date(self):
        return jalali_converter(self.date)

    def __str__(self):
        return self.user.first_name + "" + self.user.last_name
