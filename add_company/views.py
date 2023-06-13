from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from add_company.froms import UserCreationCompany, UserCreationShop
from afas.models import User, Company, Comapany_client_id, Comapany_Cl_id_AND_shops, shops


def add_comp(request):
    if request.method == 'POST':
        form = UserCreationCompany(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            field = data['company_name'] # Узанем у формы название компании
            us = User.objects.get(username=request.user.username) # Узнаем usera сессии

            a = User.objects.filter(username=us).values_list('pk', flat=True)   # Узнаем pk usera
            print(a)
            b = Company.objects.filter(company_name=field).values_list('pk', flat=True)     # Узнаем pk компании
            print(b)
            PIKEY = Comapany_client_id.objects.create(client_id=a, comp_id=b)   # Добавляем в табл Comapany_client_id pk usera и компании
            PIKEY.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/add/shop/')
    else:
        us = User.objects.get(username= request.user.username)
        form = UserCreationCompany(request.POST, request.FILES)

        return render(request, 'add_company/add_objects.html',{'form': form})


def add_shop(request):
    if request.method == 'POST':
        form_shop = UserCreationShop(request.POST,user=request.user)
        if form_shop.is_valid():
            form_shop.save()
            data = form_shop.cleaned_data
            field = data['shops_name'] # Узанем у формы название компании
            us = User.objects.get(username=request.user.username) # Узнаем usera сессии     ОСТАВИТЬ

            a = User.objects.filter(username=us).values_list('pk', flat=True)   # Узнаем pk usera   ОСТАВИТЬ
            #a1 = Comapany_client_id.objects.filter(client_id=a).order_by('pk').first()   # Узнать в моделе последний pk юзера
            a1 = Comapany_client_id.objects.filter(client_id__in=a).last()
            pk_value=a1.pk

            b = shops.objects.filter(shops_name=field).values_list('pk', flat=True)     # Узнаем pk компании
            PIKEY  = Comapany_Cl_id_AND_shops.objects.create(Comapany_Cl_id_id=pk_value, Shops_id_id=b)  # Добавляем в табл Comapany_client_id pk usera и компании
            PIKEY.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        form_shop = UserCreationShop(request.POST, user=request.user)

        return render(request, 'add_company/add_objects_shop.html', {'form_shop': form_shop})





# a = User.objects.filter(username=us).values_list('pk', flat=True)
# a1 = Comapany_client_id.objects.filter(client_id=a).last()  №1 Узнаем последнию запись
# a2 = a1.pk узнаем PK


# b = shops.objects.filter(shops_name = 'Пати').values_list('pk', flat=True)
# pks = Comapany_Cl_id_AND_shops.objects.create(Comapany_Cl_id_id=a, Shops_id_id=b)