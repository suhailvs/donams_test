from django.db import models

# Create your models here.
from django.forms import ModelForm

class UserDetail(models.Model):

    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)

class UserDetailForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = '__all__'

