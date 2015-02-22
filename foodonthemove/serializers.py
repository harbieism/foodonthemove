from django.forms import widgets
from rest_framework import serializers
from foodonthemove.models import Account


class AccountSerializer(serializers.Serializer):
    email = serializers.EmailField(required= False, allow_blank=True)
    username = serializers.CharField(required=True, max_length=40)
    phone_number = serializers.CharField(max_length=40)

    contact_text = serializers.BooleanField()
    contact_call = serializers.BooleanField()
    contact_email = serializers.BooleanField()

    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)

    is_admin = serializers.BooleanField()

    address = serializers.CharField(max_length=40, allow_blank=True)
    zip_code = serializers.CharField(max_length=20, allow_blank=True)

    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()



    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.contact_text = validated_data.get('contact_text', instance.contact_text)
        instance.contact_call = validated_data.get('contact_call', instance.contact_call)
        instance.contact_email = validated_data.get('contact_email', instance.contact_email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance. address = validated_data.get('address', instance.address)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance