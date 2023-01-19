from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from storeapp.models import Company, Product, ProductDetails, Employee, EmployeeSalary, Customer, Bill, BillDetails
from storeapp.serializers import CompanySerializer, ProductSerializer, CustomerSerializer, ProductDetailsSerializer, \
    EmployeeSerializer, EmployeeSalarySerializer, BillSerializer, BillDetailsSerializer


# Create your views here.
class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True, context={"request"})
        response_dict = {"error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:

            serializer = CompanySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Company Data Saved Successfully"}
        except:
            dict_response = {"error": True, "message": "Error Saving Company Data"}

        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Updated Company Data"}

        except:
            dict_response = {"error": True, "message": "Error Updating Company Data"}

        return Response(dict_response)


class ProductDetailsViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = ProductDetails.objects.all()
        serializer = ProductDetailsSerializer(company, many=True, context={"request"})
        response_dict = {"error": False, "message": "All Product Details List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:

            serializer = ProductDetailsSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Product Details Saved Successfully"}
        except:
            dict_response = {"error": True, "message": "Error Saving Product Details"}

        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = ProductDetails.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = ProductDetailsSerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Updated Product Details"}

        except:
            dict_response = {"error": True, "message": "Error Updating Product Details"}

        return Response(dict_response)


class ProductViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = ProductSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Product Data Saved Successfully"}
        except:
            dict_response = {"error": True, "message": "Error Saving Product Data"}

        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Product.objects.all()
            product = get_object_or_404(queryset, pk=pk)
            serializer = ProductSerializer(product, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Updated Product Data"}
        except:
            dict_response = {"error": True, "message": "Error Updating Product Data"}
        return Response(dict_response)

    def list(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True, context={"request"})
        response_dict = {"error": False, "message": "All Product List Data", "data": serializer.data}
        return Response(response_dict)


class EmployeeViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Employee.objects.all()
        serializer = EmployeeSerializer(company, many=True, context={"request"})
        response_dict = {"error": False, "message": "All Employee List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:

            serializer = EmployeeSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Employee Saved Successfully"}
        except:
            dict_response = {"error": True, "message": "Error Saving Employee"}

        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Updated Employee List"}

        except:
            dict_response = {"error": True, "message": "Error Updating Employee"}

        return Response(dict_response)


class EmployeeSalaryViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = EmployeeSalary.objects.all()
        serializer = EmployeeSalarySerializer(company, many=True, context={"request"})
        response_dict = {"error": False, "message": "All Employee Salary List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:

            serializer = EmployeeSalarySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Employee Salary Saved Successfully"}
        except:
            dict_response = {"error": True, "message": "Error Saving Employee Salary"}

        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = EmployeeSalary.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSalarySerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Updated Employee Salary List"}

        except:
            dict_response = {"error": True, "message": "Error Updating Employee Salary"}

        return Response(dict_response)


class CustomerViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Customer.objects.all()
        serializer = CustomerSerializer(company, many=True, context={"request"})
        response_dict = {"error": False, "message": "All Customer List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:

            serializer = CustomerSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Customer Saved Successfully"}
        except:
            dict_response = {"error": True, "message": "Error Saving Customer"}

        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Customer.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CustomerSerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Updated Customer List"}

        except:
            dict_response = {"error": True, "message": "Error Updating Customer"}

        return Response(dict_response)


class BillViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Bill.objects.all()
        serializer = BillSerializer(company, many=True, context={"request"})
        response_dict = {"error": False, "message": "All Bills List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:

            serializer = BillSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Bills Saved Successfully"}
        except:
            dict_response = {"error": True, "message": "Error Saving Bills"}

        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Bill.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = BillSerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Updated Bills"}

        except:
            dict_response = {"error": True, "message": "Error Updating Bills"}

        return Response(dict_response)


class BillDetailsViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = BillDetails.objects.all()
        serializer = BillDetailsSerializer(company, many=True, context={"request"})
        response_dict = {"error": False, "message": "All Bill Details List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:

            serializer = BillDetailsSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Bill Details Saved Successfully"}
        except:
            dict_response = {"error": True, "message": "Error Saving Bill Details"}

        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = BillDetails.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = BillDetailsSerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Updated Bill Details List"}

        except:
            dict_response = {"error": True, "message": "Error Updating Bill Details"}

        return Response(dict_response)


company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})
