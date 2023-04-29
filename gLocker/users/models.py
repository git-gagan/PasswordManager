from django.db import models
import uuid

class tbl_users(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=24)

class tbl_userdata(models.Model):
    id = models.AutoField(primary_key=True)
    website = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=24)
    user = models.ForeignKey(tbl_users, on_delete=models.CASCADE, null=True)
  