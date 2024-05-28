from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orderplaced/',views.orderplaced),
    path('register/user/',views.customerRegister,name='register'),
    path('login/user/',views.customerLogin,name='login'),
    path('login/banquet/',views.restLogin,name='rlogin'),
    path('register/banquet/',views.restRegister,name='rregister'),
    path('profile/banquet/',views.restaurantProfile,name='rprofile'),
    path('profile/user/',views.customerProfile,name='profile'),
    path('user/create/',views.createCustomer,name='ccreate'),
    path('user/update/<int:id>/',views.updateCustomer,name='cupdate'),
    path('banquet/create/',views.createRestaurant,name='rcreate'),
    path('banquet/update/<int:id>/',views.updateRestaurant,name='rupdate'),
    path('banquet/orderlist/',views.orderlist,name='orderlist'),
    path('banquet/menu/',views.menuManipulation,name='mmenu'),
    path('logout/',views.Logout,name='logout'),
    path('checkout/',views.checkout,name='checkout'),


    #click of banquet category will come and on click of category menu item will come, current flow is 


    path('banquet/', views.banquet, name='banquet'),
    path('banquet/<int:banquet_id>/categories/', views.getAllCategories, name='categories'),
    path('banquet/<int:banquet_id>/category/<int:category_id>/', views.banquetMenu, name='menu'),


]