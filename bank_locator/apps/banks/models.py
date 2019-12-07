"""Banking models"""
from django.db import models


class BankModel(models.Model):
    """Bank model"""
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=49, null=False)

    class Meta:
        """DB specific meta details"""
        db_table = 'banks'


class BranchModel(models.Model):
    """Branch model"""
    ifsc = models.CharField(max_length=11, primary_key=True, null=False)
    bank = models.ForeignKey(to=BankModel, on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    class Meta:
        """DB specific meta details"""
        db_table = 'branches'
