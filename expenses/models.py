from django.db import models
from django.contrib.auth.models import User

# Define the choices for the Category field
CATEGORY_CHOICES = [
    ('Health', 'Health'),
    ('Electronics', 'Electronics'),
    ('Travel', 'Travel'),
    ('Education', 'Education'),
    ('Books', 'Books'),
    ('Others', 'Others'),
]

class Expense(models.Model):
    name = models.CharField(max_length=140, verbose_name='Name of Expense')
    date_of_expense = models.DateField(verbose_name='Date of Expense')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(verbose_name='Description')
    amount = models.PositiveIntegerField(verbose_name='Amount', default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
