from rest_framework import serializers


class UserBalanceSerializer(serializers.Serializer):
    balance = serializers.FloatField()
    user = serializers.CharField()


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=36)
    date = serializers.DateField()
    category = serializers.CharField(max_length=24)
    amount = serializers.FloatField()
    user = serializers.CharField()
    kind = serializers.CharField()
