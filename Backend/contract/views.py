from rest_framework.viewsets import ModelViewSet

from .models import Contract, ContractType, Photo, Receipt
from .serializers import ContractSerializer, ContractTypeSerializer, ReceiptSerializer


class ContractTypeViewSet(ModelViewSet):
    queryset = ContractType.objects.all()
    serializer_class = ContractTypeSerializer


class ReceiptViewSet(ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    search_fields = [
        "first_name",
        "last_name",
    ]


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    search_fields = [
        "national_code",
        "contract_number",
        "contract_type",
        "car_name",
    ]
