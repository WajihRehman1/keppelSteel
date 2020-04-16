from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
app_name='basic_app'

urlpatterns = [
    path('',views.index,name='index'),
    # path('panels/',views.panelView,name='panels'),
    # path('Welding/',views.weldView,name='weld'),
    path('<int:pk>/',views.svc.as_view(), name='services'),
    path('createSvc/',login_required(views.createService.as_view()),name='createSvc'),
    path('createProduct/', login_required(views.createProuct.as_view()), name='createProduct'),
    path('login/',views.adminLogin,name='login'),
    path('update/<int:pk>/', login_required(views.UpdateService.as_view()), name='update'),
    path('updateProduct/<int:pk>/', login_required(views.UpdateProduct.as_view()), name='updateProduct'),
    path('deleteProduct/<int:pk>/', login_required(views.deleteProduct.as_view()), name='deleteProduct'),

]
