# manually created serializers.py file created to turn DB data into JSON to be used by frontend
from rest_framework import serializers
from .models import Order, OrderFlpItem, OrderTrackItem

# import serializers from flp and track apps
from flps_app.serializers import FlpSerializer
from tracks_app.serializers import TrackSerializer

# OrderItem Flp Serializer
class OrderItemFlpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFlpItem
        fields = (
            "flp",
        )

# OrderItem Track Serializer
class OrderItemTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTrackItem
        fields = (
            "track",
        )

        
# Order Flp Serializer
class OrderFlpSerializer(serializers.ModelSerializer):

    flp_items = OrderItemFlpSerializer(many=True)

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
            "flp_items",
        )

    def create(self, validated_data):
        flp_items_data = validated_data.pop('flp_items')

        try:
            flp_order = Order.objects.create(**validated_data)
        except:
            pass


        for item_data in flp_items_data:
            OrderFlpItem.objects.create(order=flp_order, **item_data)
        
        return flp_order


# Order Track Serializer
class OrderTrackSerializer(serializers.ModelSerializer):

    track_items = OrderItemTrackSerializer(many=True)


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
            "track_items",
        )

    def create(self, validated_data):
        track_items_data = validated_data.pop('track_items')

        try:
            track_order = Order.objects.create(**validated_data)
        except:
            pass


        for item_data in track_items_data:
            OrderTrackItem.objects.create(order=track_order, **item_data)
        
        return track_order