from rest_framework.viewsets import ModelViewSet

from .models import Contract, Receipt
from .serializers import ContractSerializer, ReceiptSerializer


class ReceiptViewSet(ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    search_fields = [
        "national_code",
        "contract_number",
        "contract_type",
        "car_type",
    ]
    filterset_fields = [
        "status",
    ]
