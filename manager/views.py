from django.db.models import Q
from django.shortcuts import render

from order.models import order_Admin
from django.views.generic import TemplateView, ListView


def meneger_cllient(request):
    a = order_Admin.objects.all()
    mas = []
    for i in a:
        ij = str(i)
        user = ij.find('User ')
        product = ij[:user]  # Название : Пиво. Вид упаковки bottle Кол-во 200; пользователя-компания-магазин
        comp_cl = ij.find('Comp_Cl_id')
        use = ij[
              comp_cl:]  # Comp_Cl_id : User : 1234, Company : ООО партнер, Shop : Shop_name : пивнуха ; Дата заказа 2023-06-04 19:32:15.268628+00:00
        usi = use.find(':')
        usp = use[usi + 1:]
        sum = product + usp  # Название : Пиво. Вид упаковки bottle Кол-во 213; пользователя-компания-магазин User : admin, Company : Butik, Shop : Shop_name : Рок ; Дата заказа 2023-06-04 14:45:16.445863+00:00
        sum_1 = sum.find(' Shop_name ')
        sum_2 = sum[:sum_1]  # sumirovat
        sum_3 = sum[sum_1:]
        sum_4 = sum_3.find(':')
        plus = sum_3[sum_4 + 1:]
        plus_1 = sum_2 + plus

        mas.append(plus_1)
    return render(request, 'manager/home.html', {'all': mas[::-1],
                                                 'user': request.user})


# Название : Пиво. Вид упаковки bottle Кол-во 200; пользователя-компания-магазин User : 1234, Company : User : 1234, Company : ООО партнер, Shop : Comp_Cl_id : User : 1234, Company : ООО партнер, Shop : Shop_name : пивнуха ; Дата заказа 2023-06-04 19:32:15.268628+00:00

# Create your views here.

class SearchResultsView(ListView):
    model = order_Admin
    template_name = 'manager/home.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = order_Admin.objects.filter(
            Q(us__id=query)
        )
        return object_list

# <form action="{% url 'search_results' %}" method="get">
#  <input name="q" type="text" placeholder="Search...">
# </form>
