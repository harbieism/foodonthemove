from django.forms import widgets
from rest_framework import serializers
from foodonthemove.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account