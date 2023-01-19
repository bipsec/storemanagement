"""storemanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from storeapp import views

router = routers.DefaultRouter()
router.register("company", views.CompanyViewSet, basename="company")
router.register("product_details", views.ProductDetailsViewSet, basename="product_details")
router.register("product", views.ProductViewSet, basename="product")
router.register("employee", views.EmployeeViewSet, basename="employee")
router.register("employee_salary", views.EmployeeSalaryViewSet, basename="employee_salary")
router.register("customer", views.CustomerViewSet, basename="customer")
router.register("bill", views.BillViewSet, basename="bill")
router.register("bill_details", views.BillDetailsViewSet, basename="bill_details")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/gettoken/', TokenObtainPairView.as_view(), name="gettoken"),
    path('api/refresh_token/', TokenObtainPairView.as_view(), name="refresh_token")
]
