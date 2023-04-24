from account.models import User
from django.db import models


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
