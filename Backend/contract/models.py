from django.db import models
from extensions.utils import jalali_converter


class BaseClass(models.Model):
    CONTRACT_TYPE_CHOICES = (
        ("فروش", "فروش"),
        ("حق العملکاری", "حق العملکاری"),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_code = models.IntegerField(unique=True)
    car_name = models.CharField(max_length=100, null=True)
    car_model = models.CharField(max_length=100, null=True)
    car_Color = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPE_CHOICES)

    class Meta:
        abstract = True


class Receipt(BaseClass):
    receipt_number = models.IntegerField(unique=True)
    receipt_payment_date = models.DateField(null=True)
    receipt_amount = models.IntegerField(null=True)

    class Meta(BaseClass.Meta):
        db_table = "Receipt"

    def __str__(self):
        return str(self.receipt_number)

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
        ("تسویه شده", "تسویه شده"),
        ("تاخیر خورده", "تاخیر خورده"),
        ("تمدید شده", "تمدید شده"),
    )
    father_name = models.CharField(max_length=100, null=True)
    phone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    receipt = models.ManyToManyField(Receipt, related_name="receipts")
    contract_number = models.IntegerField(unique=True)
    number_of_car = models.IntegerField(null=True)
    car_type = models.CharField(max_length=255, null=True)
    car_delivery = models.CharField(
        max_length=50, choices=CAR_DELIVERY_CHOICES, null=True
    )
    day_of_delivery = models.IntegerField(null=True)
    month_of_delivery = models.DateField(null=True)
    month_of_commission = models.DateField(null=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="در حال انجام"
    )
    delay = models.IntegerField(null=True)

    class Meta(BaseClass.Meta):
        db_table = "Contract"
        ordering = ("created_date",)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Photo(models.Model):
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="contract/images", null=True)

    class Meta:
        db_table = "Contract Photos"
