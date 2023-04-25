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
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Manager Message"
        ordering = ("-created",)
        get_latest_by = "created"

    def __str__(self):
        return self.text
