from django import forms

from django import forms

from afas.models import Company, shops, Comapany_client_id, User


class UserCreationCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("company_name", "address")


class UserCreationShop(forms.ModelForm):
    def __init__(self ,*args, **kwargs):
        user = kwargs.pop('user')  # получаем текущего пользователя из параметров формы
        super().__init__(*args, **kwargs)
        #us = User.objects.get(username=request.user.username) # Возможна ошибка
        self.fields['comp_and_user'].queryset = Comapany_client_id.objects.filter(client= user)

    class Meta:
        model = shops
        fields = ("comp_and_user",  'shops_name')

#class UserShop(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    shop = models.OneToOneField(Shop, on_delete=models.CASCADE)
#
#    def save(self, *args, **kwargs):
#        if not self.pk:
#            # Фильтруем магазины по текущему пользователю
#            shop = Shop.objects.filter(comp_and_user__user=self.user).first()
#            if shop:
#                self.shop = shop
#        super(UserShop, self).save(*args, **kwargs)