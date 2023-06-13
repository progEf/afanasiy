"""
URL configuration for afanasiy_bd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from manager.views import meneger_cllient, SearchResultsView

from add_company.views import add_comp, add_shop
from order.views import firma_and_order312, order_user, order, update_ord, update_basket, rog_ord

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('register.urls')),
    path('add/', add_comp),
    path('add/shop/', add_shop),
    path('order/', firma_and_order312),
    path('order/shop/', order_user),
    path('order/shop/user', order),
    # path('meba/', SearchResultsView.as_view(), name='search_results')meneger_cllient
    path('meba/', meneger_cllient),
    path('up_basket/',update_basket ),  # Корзина
    path('up_ord/', update_ord),        # Заказ rog_ord
    path('up_ord/chj/', rog_ord),  # Заказ rog_ord

]
