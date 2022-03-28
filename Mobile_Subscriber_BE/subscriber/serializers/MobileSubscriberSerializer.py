from subscriber.models.MobileSubscriberModel import MobileSubscriberModel
from rest_framework import serializers


class MobileSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileSubscriberModel
        fields = [
            'id',
            'msisdn',
            'customer_id_owner',
            'customer_id_user',
            'service_type',
            'service_start_date'
        ]
        read_only_fields = ('id',)

    def to_representation(self, instance):
        formatted_datetime_field = instance.service_start_date.timestamp()

        return {
            'id': instance.id,
            'msisdn': instance.msisdn,
            'customer_id_owner': instance.customer_id_owner.id,
            'customer_id_user': instance.customer_id_user.id,
            'service_type': instance.service_type,
            'service_start_date': formatted_datetime_field
        }


class MobSubNumbersSerializer(serializers.Serializer):

    class Meta:
        model = MobileSubscriberModel
        fields = [
            'id',
            'msisdn',
            'customer_id_owner',
            'customer_id_user',
            'service_type',
            'service_start_date'
        ]

    def to_representation(self, instance):
        return {
            'msisdn': instance.msisdn,
        }


class MobSubUpdateSerializer(serializers.Serializer):

    class Meta:
        model = MobileSubscriberModel
        fields = [
            'id',
            'msisdn',
            'customer_id_owner',
            'customer_id_user',
            'service_type',
            'service_start_date'
        ]
        read_only_fields = (
            'id',
            'msisdn',
            'customer_id_owner',
            'customer_id_user',
            'service_start_date',
        )

    def to_representation(self, instance):

        formatted_datetime_field = instance.service_start_date.timestamp()

        return {
            'id': instance.id,
            'msisdn': instance.msisdn,
            'customer_id_owner': instance.customer_id_owner.id,
            'customer_id_user': instance.customer_id_user.id,
            'service_type': instance.service_type,
            'service_start_date': formatted_datetime_field
        }

    def update(self, instance, validated_data):

        instance.service_type = validated_data.get(
            'service_type',
            instance.service_type
        )
        instance.save()
        return instance
