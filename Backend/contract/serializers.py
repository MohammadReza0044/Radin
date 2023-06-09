import os

from rest_framework import serializers

from .models import Contract, Photo, Receipt


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
            "uploaded_images": {"required": False},
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

    def clear_existing_images(self, instance):
        old_images = Photo.objects.filter(contract_id=instance.id)

        for i in old_images:
            path = str(i.image.path)
            i.delete()
            os.remove(path)

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", None)
        if uploaded_images:
            self.clear_existing_images(instance)
            contract_image_model_instance = [
                Photo(contract=instance, image=image) for image in uploaded_images
            ]
            Photo.objects.bulk_create(contract_image_model_instance)
        return super().update(instance, validated_data)

    def validate(self, data):
        data_dict = dict(data)
        contract_type = data_dict.get("contract_type")
        car_delivery = data_dict.get("car_delivery")
        if contract_type == "فروش" and data_dict.get("car_delivery") == None:
            raise serializers.ValidationError(
                {"car_delivery": ["نوع تحویل باید مشخص شود"]}
            )

        if (
            contract_type == "حق العملکاری"
            and data_dict.get("month_of_commission") == None
        ):
            raise serializers.ValidationError(
                {"month_of_commission": ["ماه تحویل باید وارد شود"]}
            )
        if car_delivery == "روزانه" and data_dict.get("day_of_delivery") == None:
            raise serializers.ValidationError(
                {"day_of_delivery": ["تعداد روز تحویل باید مشخص شود"]}
            )
        if car_delivery == "ماهانه" and data_dict.get("month_of_delivery") == None:
            raise serializers.ValidationError(
                {"month_of_delivery": ["تاریخ تحویل باید مشخص شود"]}
            )

        return data
