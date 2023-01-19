from rest_framework.serializers import ModelSerializer

from storeapp.models import Company, Product, Customer, ProductDetails, Employee, EmployeeSalary, Bill, BillDetails


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProductDetailsSerializer(ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company_id).data
        return response


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeSalarySerializer(ModelSerializer):
    class Meta:
        model = EmployeeSalary
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerializer(instance.emp_id).data
        return response


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BillSerializer(ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.cust_id).data
        return response


class BillDetailsSerializer(ModelSerializer):
    class Meta:
        model = BillDetails
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bill'] = BillSerializer(instance.bill_id).data
        return response
