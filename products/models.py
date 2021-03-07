from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class DeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)


class Product(models.Model):
    titles = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = ActiveManager()
    deleted = DeletedManager()

    def __str__(self):
        return f"{self.title} - {self.date_created}"