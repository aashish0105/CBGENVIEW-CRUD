from django.db import models

del_choices=(
    ('Pending','Pending'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered')
)

# Create your models here.
class Laptop(models.Model):
    Company=models.CharField(max_length=30)
    Processor=models.CharField(max_length=30)
    Ram=models.IntegerField()
    Price=models.FloatField()
    Del_status=models.CharField(max_length=30,choices=del_choices)
    Purchasedate=models.DateField()
    is_paid = models.BooleanField()
