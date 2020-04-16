from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from . import models
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, logout, login


# Create your views here.

def index(request):
    svc = models.services.objects.all()
    return render(request, 'basic_app/index.html', {'obj': svc})


class svc(DetailView):
    context_object_name = 'myObj'
    model = models.services
    template_name = 'basic_app/showProducts.html'


class createService(CreateView):
    fields = ('name', 'description', 'picture')
    model = models.services


class createProuct(CreateView):
    fields = ('services','title', 'description', 'picture')
    model = models.svcItems


def adminLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('basic_app:index'))

            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse("Wroong details")
    else:
        return render(request, 'basic_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:index'))


class UpdateService(UpdateView):
    model = models.services
    fields = ('name', 'description', 'picture')


class UpdateProduct(UpdateView):
    model = models.svcItems
    fields = ('services','title' ,'description', 'picture')


class deleteProduct(DeleteView):
    context_object_name = 'product'
    model = models.svcItems
    success_url = reverse_lazy("basic_app:index")