from rest_framework import serializers
class ProductSerializer (serializers.Serializer):
    p_id = serializers.IntegerField()
    p_name = serializers.CharField(max_length=30)
    p_cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    p_mfd = serializers.DateField()
    p_exd = serializers.DateField()