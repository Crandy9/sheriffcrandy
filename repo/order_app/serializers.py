# manually created serializers.py file created to turn DB data into JSON to be used by frontend
from rest_framework import serializers
from .models import Order, OrderItem

# import serializers from flp and track apps
from flps_app.serializers import FlpSerializer
from tracks_app.serializers import TrackSerializer

# OrderItem Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            # price, flp, track, quantity
            # flp items
            "flp",
            "usd_flp_price",
            "jpy_flp_price",
            "flp_quantity",
            # track items
            "track",
            "usd_track_price",
            "jpy_track_price",
            "track_quantity",
        )

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):

    # get related names from Order model
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            "id",
            "name",
            "email",
            "phone",
            "address1",
            "address2",
            "statePref",
            "country",
            "zipcode",
            "stripe_token",
            "items",
        )

    # override serializer create func
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order