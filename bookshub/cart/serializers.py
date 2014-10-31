from rest_framework import serializers

from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem

    def validate(self, attrs):
        quantity = attrs['quantity']
        offer = attrs['offer']
        buyer = attrs['user']

        if buyer == offer.owner:
            message = 'Invalid action, you can not buy your own book.'
            raise serializers.ValidationError(message)

        if quantity > offer.quantity:
            message = 'The quantity entered is not valid.'
            raise serializers.ValidationError(message)

        return attrs