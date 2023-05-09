from account.models import User
from django.db import models
from django.db.models.functions import Now


class ToDoManager(models.Manager):
    def expired(self):
        return self.filter(created__lt=Now())


class ToDoList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "To Do List"
        ordering = ("-created",)

    def __str__(self):
        return self.title

    objects = ToDoManager()


class ManagerMessage(models.Model):
    title = models.CharField(max_length=255, null=True)
    text = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="manager message/images", null=True)
    video = models.FileField(
        upload_to="manager message/video",
        null=True,
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Manager Message"
        ordering = ("-created",)
        get_latest_by = "created"

    def __str__(self):
        return self.title


class WorkingMonth(models.Model):
    title = models.CharField(max_length=255, null=True)
    working_month = models.DateField()

    class Meta:
        db_table = "Working Month"


class WorkingDay(models.Model):
    month = models.ForeignKey(
        WorkingMonth, on_delete=models.CASCADE, related_name="working_days"
    )
    working_day = models.DateField()

    class Meta:
        db_table = "Working Day"
