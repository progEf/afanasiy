from django.contrib import admin

# Register your models here.
from order.models import product_admin,User_Comp_Shop, product_discount


admin.site.register(product_admin)
admin.site.register(product_discount)

admin.site.register(User_Comp_Shop)
