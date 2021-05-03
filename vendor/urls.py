from django.urls import path
from . import views

app_name='vendor'

urlpatterns = [
	path('businesswork/', views.businesswork),
    path('addvendor/',views.addvendor),
    path('import/',views.IProduct),
    path('export/',views.EProduct),
    path('view-vendors/',views.ViewVendors),
    path('category/',views.Category),
    path('addcategory/',views.AddCategory),
    path('view-import/',views.ViewImport),
    path('sortbyvendor/<int:id>/',views.sortbyvendor, name='byvendor'),
    path('mystore/',views.mystore),
    path('bycategory/<int:id>/',views.bycategory,name='category'),
    path('export/',views.EProduct),
    path('customer_detail/',views.customer_detail),
    path('billing/',views.billing),
    path('customer_bill/<int:id>/',views.customer_bill,name='by_customer'),
    path('about_customer/<int:id>/',views.about_customer, name='about_customer'),
    path('about/',views.about),
    path('s/',views.searchCust, name='search'),
    path('v/',views.searchVendor, name='search'),
    path('p/',views.searchPro, name='search'),
    path('view-export/', views.view_export),
    path('export_by_date/<int:id>/',views.export_by_date, name='by_date'),


]
