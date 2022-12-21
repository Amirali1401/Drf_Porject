from django.urls import path

from . import views as product_views

urlpatterns = [
    path('list_products/' , product_views.ListViewsProduct.as_view() , name = 'list_products'),
    path('create_product/' , product_views.CreateViewProduct.as_view() , name = 'create_product'),
    path('<int:product_id>/update_product/' , product_views.UpdateViewProduct.as_view() , name = 'update_product'),
    path('<int:product_id>/delete_product/',product_views.DeleteViewProduct.as_view() , name='delete_product'),
    ]