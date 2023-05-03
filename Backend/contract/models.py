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


class Receipt(BaseClass):
    contract_type = models.ForeignKey(
        ContractType, on_delete=models.SET_NULL, null=True
    )
    receipt_number = models.IntegerField()
    receipt_payment_date = models.DateField(null=True)
    receipt_amount = models.IntegerField(null=True)

    class Meta(BaseClass.Meta):
        db_table = "Receipt"

    def jalali_date(self):
        return jalali_converter(self.receipt_payment_date)


class Contract(BaseClass):
    CONTRACT_TYPE_CHOICES = (
        ("فروش", "فروش"),
        ("حق العملکاری", "حق العملکاری"),
    )
    CAR_DELIVERY_CHOICES = (
        ("روزانه", "روزانه"),
        ("ماهانه", "ماهانه"),
    )
    STATUS_CHOICES = (
        ("در حال انجام", "در حال انجام"),
        ("اتمام قرارداد", "اتمام قرارداد"),
        ("تاخیر قرارداد", "تاخیر قرارداد"),
        ("تمدید قرارداد", "تمدید قرارداد"),
    )
    father_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    receipt = models.ManyToManyField(Receipt, related_name="receipt")
    contract_number = models.IntegerField(unique=True)
    car_number = models.IntegerField()
    contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPE_CHOICES)
    car_delivery = models.CharField(
        max_length=50, choices=CAR_DELIVERY_CHOICES, null=True
    )
    day_of_delivery = models.IntegerField(null=True)
    month_of_delivery = models.DateField(null=True)
    month_of_commission = models.DateField(null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    image = models.ImageField(upload_to="contract/images", null=True)

    class Meta(BaseClass.Meta):
        db_table = "Contract"

    def jalali_date_delivery(self):
        return jalali_converter(self.month_of_delivery)

    def jalali_date_commission(self):
        return jalali_converter(self.month_of_commission)


class Photo(models.Model):
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="contract/images", null=True)

    class Meta:
        db_table = "Photo"
