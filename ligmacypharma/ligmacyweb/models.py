from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    age = models.IntegerField()

    class Meta:
        db_table = "accounts"


class Medicine(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    stock = models.IntegerField()

    class Meta:
        db_table = "medicine"