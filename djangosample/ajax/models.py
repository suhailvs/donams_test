from django.db import models

# Create your models here.
from django import forms
from django.core.validators import validate_email

class UserDetail(models.Model):
	fullname = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	contact = models.CharField(max_length=50)
	address1 = models.CharField(max_length=200)
	address2 = models.CharField(max_length=200)

class UserDetailForm(forms.ModelForm):
	def clean_email(self):
		email = self.cleaned_data['email']
		if UserDetail.objects.filter(email=email):
			raise forms.ValidationError("email already exist!")
		return email

	class Meta:
		model = UserDetail
		fields = '__all__'

