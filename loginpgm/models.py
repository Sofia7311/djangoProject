from django.db import models
from django.forms import ModelForm

# Create your models here.


class Loginsetup(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    loginid = models.CharField(max_length = 254)
    loginpassword = models.CharField(max_length = 50)
    #contact_number = models.CharField(max_length = 100)

#class RegisterForm(ModelForm):
 #   class Meta:
  #      model = Loginsetup
   #     fields = ['first_name', 'last_name', 'loginid', 'loginpassword']

# Create your models here.
