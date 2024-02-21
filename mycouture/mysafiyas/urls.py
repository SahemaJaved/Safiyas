from . import views
from django.urls import path

urlpatterns = [
    path('',views.allproducts, name='allproducts'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('aboutus/',views.about_us,name='aboutus'),
    path('feedback/',views.feed_back,name='feedback'),
    path('home/',views.home,name='home'),
    path('Cart/',views.view_cart,name="view_cart"),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('<slug:slug_c>/', views.allproducts, name='product_by_category'),
    path('<slug:slug_c>/<slug_p>/', views.prod_det, name='product_catdetail'),
]