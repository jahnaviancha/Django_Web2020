from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email_address=models.EmailField(max_length=25)
    password=models.CharField(max_length=15)
    confirm_password=models.CharField(max_length=15)

    class Meta:
        db_table= 'customer'
