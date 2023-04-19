from django.db import models
from extensions.utils import jalali_converter


class BaseClass(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_code = models.IntegerField()
    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_Color = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name + " " + self.last_name


class ContractType(models.Model):
    type = models.CharField(max_length=200)

    class Meta:
        db_table = "Contract Type"

    def __str__(self):
        return self.type


class ContractDuration(models.Model):
    type = models.CharField(max_length=200)

    class Meta:
        db_table = "Contract Duration"

    def __str__(self):
        return self.type


class ContractProfit(models.Model):
    type = models.CharField(max_length=200)

    class Meta:
        db_table = "Contract Profit"

    def __str__(self):
        return self.type


class ContractDurationType(models.Model):
    type = models.CharField(max_length=200)

    class Meta:
        db_table = "Contract Duration Type"

    def __str__(self):
        return self.type


class Receipt(BaseClass):
    contract_type = models.ForeignKey(
        ContractType, on_delete=models.SET_NULL, null=True
    )
    receipt_number = models.IntegerField()
    receipt_payment_date = models.DateField()
    receipt_amount = models.IntegerField()

    class Meta(BaseClass.Meta):
        db_table = "Receipt"

    def jalali_date(self):
        return jalali_converter(self.receipt_payment_date)


class Contract(BaseClass):
    father_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    contract_type = models.ForeignKey(
        ContractType, on_delete=models.SET_NULL, null=True
    )
    contract_duration = models.ForeignKey(
        ContractDuration, on_delete=models.SET_NULL, null=True
    )
    contract_profit = models.ForeignKey(
        ContractProfit, on_delete=models.SET_NULL, null=True
    )
    contract_duration_type = models.ForeignKey(
        ContractDurationType, on_delete=models.SET_NULL, null=True
    )

    class Meta(BaseClass.Meta):
        db_table = "Contract"
