from rest_framework.viewsets import ModelViewSet

from .models import Contract
from .serializers import ContractSerializer


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
