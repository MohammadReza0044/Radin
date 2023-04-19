from rest_framework.viewsets import ModelViewSet

from .models import Receipt
from .serializers import ReceiptSerializer


class UserViewSet(ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    search_fields = [
        "first_name",
        "last_name",
        "personal_number",
        "phone_number",
    ]
