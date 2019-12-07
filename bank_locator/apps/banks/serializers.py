"""Bank serializers"""
from rest_framework import serializers

from .models import BankModel, BranchModel


class BankSerializer(serializers.ModelSerializer):
    """Bank serializer"""
    class Meta:
        """Meta class for model specific details"""
        model = BankModel
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    """Bank serializer"""
    bank = BankSerializer(read_only=True)

    class Meta:
        """Meta class for model specific details"""
        model = BranchModel
        fields = '__all__'


class BranchSlimSerializer(serializers.ModelSerializer):
    """Branch serializer given a bank and city"""
    bank = BankSerializer(read_only=True)

    class Meta:
        """Meta class for model specific details"""
        model = BranchModel
        exclude = ('ifsc', 'address')
