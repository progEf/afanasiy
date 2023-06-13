from django.contrib import admin

# Register your models here.
from afas.models import User, Company, Comapany_client_id, shops, Comapany_Cl_id_AND_shops

admin.site.register(Company)
admin.site.register(Comapany_client_id)
admin.site.register(shops)
admin.site.register(Comapany_Cl_id_AND_shops)
