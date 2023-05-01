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
        extra_kwargs = {
            "car_delivery": {"required": False},
            "day_of_delivery": {"required": False},
            "month_of_delivery": {"required": False},
            "month_of_commission": {"required": False},
        }

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        receipts = validated_data.pop("receipt")
        contract = Contract.objects.create(**validated_data)
        for image in uploaded_images:
            newcontract_image = Photo.objects.create(contract=contract, image=image)
        contract.receipt.set(receipts)
        return contract

    def validate(self, data):
        data_dict = dict(data)
        contract_type = data_dict.get("contract_type")
        car_delivery = data_dict.get("car_delivery")
        if contract_type == "SALE" and data_dict.get("car_delivery") == None:
            raise serializers.ValidationError(
                {"car_delivery": ["نوع تحویل باید مشخص شود"]}
            )

        if (
            contract_type == "COMMISSION"
            and data_dict.get("month_of_commission") == None
        ):
            raise serializers.ValidationError(
                {"month_of_commission": ["ماه تحویل باید وارد شود"]}
            )
        if car_delivery == "DAILY" and data_dict.get("day_of_delivery") == None:
            raise serializers.ValidationError(
                {"day_of_delivery": ["تعداد روز تحویل باید مشخص شود"]}
            )
        if car_delivery == "MONTHLY" and data_dict.get("month_of_delivery") == None:
            raise serializers.ValidationError(
                {"month_of_delivery": ["تاریخ تحویل باید مشخص شود"]}
            )

        return data
