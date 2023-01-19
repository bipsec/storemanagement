from django.db import models


# Create your models here.

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "company"


class ProductDetails(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=255)
    in_stock = models.IntegerField()
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "product_details"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    mfg_date = models.DateField()
    exp_date = models.DateField()
    in_stock = models.IntegerField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    added_on = models.CharField(max_length=255)
    objects = models.Manager()

    class Meta:
        db_table = "product"


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    join_date = models.DateField()
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "employee"


class EmployeeSalary(models.Model):
    id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_date = models.DateTimeField()
    salary_amount = models.FloatField()
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = "employee_salary"


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = 'customer'


class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = 'bill'


class BillDetails(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        db_table = 'bill_details'


