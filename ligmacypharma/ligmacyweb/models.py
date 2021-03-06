from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

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


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    items_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        db_table = "cart"

# class UserSession(models.Model):
#     user= models.ForeignKey(User, on_delete=models.CASCADE)
#     session=models.ForeignKey(Session)

class CartItem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    items_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        db_table = "cartItem"