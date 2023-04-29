from rest_framework import serializers

from .models import Contract, ContractType, Photo, Receipt


class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = "__all__"


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    images = PhotoSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000, allow_empty_file=False, use_url=False
        ),
        write_only=True,
    )

    class Meta:
        model = Contract
        fields = "__all__"

    def perform_create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        receipts = validated_data.pop("receipt")
        contract = Contract.objects.create(**validated_data)
        for image in uploaded_images:
            newcontract_image = Photo.objects.create(contract=contract, image=image)

        contract.receipt.set(receipts)
        return contract
