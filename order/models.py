from django.db import models
from django.forms import DateInput
from django.utils.translation import gettext_lazy as _
# Create your models here.
from afas.models import Comapany_client_id, shops, User, Comapany_Cl_id_AND_shops


class User_Comp_Shop(models.Model):
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #Comapany_Cl_id = models.ForeignKey(Comapany_client_id, on_delete=models.CASCADE)
    Shops_id = models.ForeignKey(Comapany_Cl_id_AND_shops, on_delete=models.CASCADE, null=True)
    status_procent = models.IntegerField(null=True)
    id_rundom = models.IntegerField(null=True)



    def __str__(self):
        return f'User : {self.client_id}, Shop : {self.Shops_id} '

class key_User_Comp_Shop(models.Model):
    client_id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    key_comp = models.ForeignKey(User_Comp_Shop, on_delete=models.CASCADE)




class product_admin(models.Model):
    Unit_dimensions = [
        ('bottle', 'bottle '),
        ('packaging', 'packaging')
    ]

    product_name = models.CharField(max_length=200)
    el = models.CharField(max_length=200, choices=Unit_dimensions,null = True )
    price = models.IntegerField(null = True)

    def __str__(self):
        return f'Название : {self.product_name}. Вид упаковки {self.el} Цена {self.price}'





class product_discount(models.Model):
    Unit_dimensions = [
        ('bottle', 'bottle '),
        ('packaging', 'packaging')
    ]

    product_name = models.CharField(max_length=200)
    el = models.CharField(max_length=200, choices=Unit_dimensions, null=True)
    stat_time = models.DateField(null=True)
    end_time = models.DateField( null=True)
    price = models.IntegerField(null = True)

    def __str__(self):

        return f'Название : {self.product_name}. Вид упаковки {self.el}. Начало акции {self.stat_time} Конец акции {self.end_time} Цена {self.price}'




class order_products_user(models.Model):
    id_us = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User_Comp_Shop, on_delete=models.CASCADE)
    id_product = models.ForeignKey(product_admin, on_delete=models.CASCADE, null=True)
    id_product_discont = models.ForeignKey(product_discount, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()
    sumir = models.IntegerField(null=True)
    #stat_time = models.DateField(null=True)

    def __str__(self):

        return f'{self.id_product or self.id_product_discont} Кол-во {self.amount} Общая сумма : {self.sumir}'



class order_companu(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_comp = models.ForeignKey(User_Comp_Shop, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id_comp}'




class order_Admin(models.Model):
    us = models.ForeignKey(order_products_user, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User_Comp_Shop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    data_time = models.DateField(null=True)

    def __str__(self):
        return f'{self.us}; пользователя-компания-магазин {self.user_id}; Дата заказа {self.data_time}'