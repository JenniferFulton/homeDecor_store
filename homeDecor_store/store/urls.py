from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('new_item', views.new_item),
    path('new_warehouse', views.new_warehouse),
    path('warehouse_success', views.warehouse_success),
    path('item_success', views.item_success),
    path('edit_item/<int:id>', views.edit_item),
    path('edit_success/<int:id>', views.edit_success),
    path('delete_item', views.delete_item),
]