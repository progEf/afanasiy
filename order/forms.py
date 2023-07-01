from urllib import request

from django import forms

from afas.models import Company, shops, Comapany_client_id, User, Comapany_Cl_id_AND_shops
from order.models import User_Comp_Shop, product_admin, order_products_user, order_Admin, order_companu, \
    product_discount, key_User_Comp_Shop

from django.db.models import Q
class UserCompShop(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        client_id = User.objects.filter(username=user).values_list('id', flat=True).get()
        self.fields['client_id'].queryset = User.objects.filter(id=client_id)
       # self.fields['Comapany_Cl_id'].queryset = Comapany_client_id.objects.filter(client_id=client_id)
        self.fields['Shops_id'].queryset = Comapany_Cl_id_AND_shops.objects.filter(user_ids_id = client_id)
        self.fields['id_rundom'].required = False
        self.fields['id_rundom'].widget = forms.HiddenInput()

    class Meta:
        model = User_Comp_Shop
        fields = ['client_id', 'Shops_id', 'id_rundom']


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = product_admin
        fields = ('product_name', 'el')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs['readonly'] = True

    def clean_product_name(self):
        return self.instance.product_name


class Product_Amout(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        client_id = User.objects.filter(username=user).values_list('id', flat=True).get()
        client_id_1 = User.objects.get(username=user)
        #       form.fields['field_name'].widget = forms.HiddenInput()
        find_user_com=key_User_Comp_Shop.objects.filter(client_id_user_id = client_id).values_list('key_comp', flat=True)
        self.fields['id_user'].queryset = User_Comp_Shop.objects.filter(id=find_user_com[0])
        self.fields['id_us'].queryset = User.objects.filter(username=client_id_1)
        diskont = User_Comp_Shop.objects.filter(id= find_user_com[0]).values_list('status_procent', flat=True)
        try:
            if diskont[0] == 0 or diskont[0] == None:
                self.fields['id_product_discont'].required = False
                self.fields['id_product_discont'].widget = forms.HiddenInput()
            else:

                self.fields['id_product'].required = False
                self.fields['id_product_discont'].required = False
        except:
            self.fields['id_product'].required = False
            self.fields['id_product_discont'].required = False

        #self.fields['id_product_discont'].widget = forms.HiddenInput()


    class Meta:
        model = order_products_user
        fields = ['id_user', 'id_product', 'id_product_discont', 'amount', 'id_us']


class Product_order_user(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        client_id = User.objects.filter(username=user).values_list('id', flat=True).get()
      #  client_id_comp = order_products_user.objects.filter(id_us=user,id_user_id = com ).values_list('id', flat=True).get()
        find_user_com=key_User_Comp_Shop.objects.filter(client_id_user_id = client_id).values_list('key_comp', flat=True)

        self.fields['user_id'].queryset = User_Comp_Shop.objects.filter(id=find_user_com[0])  # 1, 5, 5 ,


    class Meta:
        model = order_Admin

        fields = ['data_time', 'user_id']



class update_ord_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')

        super().__init__(*args, **kwargs)
        client_id = User.objects.filter(username=user).values_list('id', flat=True).get()   # id
        client_id_1 = User.objects.get(username=user) # name
        shopik = order_companu.objects.filter(id_user_id=client_id).values_list('id_comp',
                                                                                flat=True).first()  # Узнаем магаз id
        find_user_com = key_User_Comp_Shop.objects.filter(client_id_user_id=client_id).values_list('key_comp', flat=True)


        self.fields['id_user'].queryset = User_Comp_Shop.objects.filter(id=find_user_com[0])
        self.fields['id_us'].queryset = User.objects.filter(username=client_id_1)
        id_prod = order_products_user.objects.filter(id_user_id= find_user_com[0]).exclude(id_product_id=None).values_list('id_product', flat=True)
        id_prod_dis = order_products_user.objects.filter(id_user_id= find_user_com[0]).exclude(id_product_id=None).values_list('id_product_discont', flat=True)



        self.fields['amount'].required = False
        diskont = User_Comp_Shop.objects.filter(id=find_user_com[0]).values_list('status_procent', flat=True)
        try:
            if diskont[0] == 0 or diskont[0] == None:
                self.fields['id_product_discont'].required = False
                self.fields['id_product_discont'].widget = forms.HiddenInput()
                self.fields['id_product'].queryset = product_admin.objects.filter(Q(id__in=id_prod))

            else:
                self.fields['id_product'].queryset = product_admin.objects.filter(Q(id__in=id_prod))
                self.fields['id_product_discont'].queryset = product_discount.objects.filter(Q(id__in=id_prod_dis))


                self.fields['id_product'].required = False
                self.fields['id_product_discont'].required = False
        except:
            self.fields['id_product'].queryset = product_admin.objects.filter(Q(id__in=id_prod))
            self.fields['id_product_discont'].queryset = product_discount.objects.filter(Q(id__in=id_prod_dis))

            self.fields['id_product'].required = False
            self.fields['id_product_discont'].required = False




    class Meta:
        model = order_products_user

        fields = ['id_us','id_user', 'id_product', 'id_product_discont', 'amount']


class choice_company(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')

        super().__init__(*args, **kwargs)
        client_id = User.objects.filter(username=user).values_list('id', flat=True).get()   # id


        client_id_1 = User.objects.get(username=user)
        find_user_com=key_User_Comp_Shop.objects.filter(client_id_user_id = client_id).values_list('key_comp', flat=True)


        client_id = User.objects.filter(username=user).values_list('id', flat=True).get()   # i
        self.fields['id_user'].queryset = User.objects.filter(username=client_id_1)

        self.fields['id_comp'].queryset = User_Comp_Shop.objects.filter(id=find_user_com[0])



    class Meta:
        model = order_companu

        fields = ['id_user', 'id_comp']
