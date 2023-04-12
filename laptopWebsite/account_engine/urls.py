from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('checkout/', views.checkout, name='checkout'),
    path('single-product/', views.single_product, name='single_product'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login-Signup/', views.login_Signup, name='login_Signup'),

]
