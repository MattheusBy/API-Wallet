from django.db import models
from django.contrib.auth.models import User


class UserBalance(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    balance = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user} Balance:{self.balance}"


class Transaction(models.Model):
    description = models.CharField(max_length=36)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=24)
    amount = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kind = models.CharField(max_length=24, default="Расход")

    def __str__(self):
        return f" {self.kind} {self.amount} - {self.user}"
