from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.


#class user_id(models.Model):
#    login = models.CharField(max_length=20)
#    password = models.CharField(max_length=20)  # Таблица 1
#    client_id = models.CharField(max_length=20, primary_key=True)
#
#    def __str__(self):
#        return f'{self.login}, {self.client_id}'
#

class User(AbstractUser):
    #client_id = models.CharField(max_length=20)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

    phone_user = models.CharField(validators = [phoneNumberRegex], max_length = 11, null=False)

    #def __str__(self):
    #    return  f'Номер телефона {self.phone_user}'


class Company(models.Model):
    company_name = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True)
   # company_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.company_name}'


class Comapany_client_id(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    comp = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'User : {self.client}, Company : {self.comp}'


class shops(models.Model):
    comp_and_user = models.ForeignKey(Comapany_client_id, on_delete=models.CASCADE)
    #shops_id = models.CharField(max_length=20)
    shops_name = models.CharField(max_length=20)

    def __str__(self):
        return f'Shop_name : {self.shops_name}'


class Comapany_Cl_id_AND_shops(models.Model):
    Comapany_Cl_id = models.ForeignKey(Comapany_client_id, on_delete=models.CASCADE)
    Shops_id = models.ForeignKey(shops, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comp_Cl_id : {self.Comapany_Cl_id}, Shop : {self.Shops_id}'



