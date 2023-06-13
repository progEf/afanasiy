from django.http import HttpResponseRedirect
from django.shortcuts import render
#from afas.forms import Create_user
# Create your views here.
#def home(request):
#    return render(request, 'home.html')
#
#def register_user(request):
#    if request.method == 'POST':
#
#        form = Create_user(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('http://127.0.0.1:8000')
#    else:
#        form = Create_user(request.POST, request.FILES)
#        return render(request, 'regist/register.html', {'form': form})
