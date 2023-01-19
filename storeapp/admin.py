from django.contrib import admin

from storeapp.models import Product, Company, ProductDetails, Customer, Bill, BillDetails,Employee, EmployeeSalary

# Register your models here.

admin.site.register(Product)
admin.site.register(Company)
admin.site.register(ProductDetails)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(BillDetails)
admin.site.register(Employee)
admin.site.register(EmployeeSalary)
