# manually created serializers.py file created to turn DB data into JSON to be used by frontend
from rest_framework import serializers
from .models import Order, OrderFlpItem, OrderTrackItem

# import serializers from flp and track apps
from flps_app.serializers import FlpSerializer
from tracks_app.serializers import TrackSerializer

# OrderItem Flp Serializer
class OrderItemFlpSerializer(serializers.ModelSerializer):
    print("WE'RE IN THE OrderItemFlpSerializer for axios post")
    class Meta:
        model = OrderFlpItem
        fields = (
            "flp",
            "usd_price",
            "jpy_price",
            "quantity",
        )

# OrderItem Track Serializer
class OrderItemTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTrackItem
        fields = (
            "track",
            "usd_price",
            "jpy_price",
            "quantity",
        )

# Order Flp Serializer
class OrderFlpSerializer(serializers.ModelSerializer):

    print("WE'RE IN THE OrderFlpSerializer for axios post")

    items = OrderItemFlpSerializer(many=True)

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
            "items",
            "stripe_token",
        )

    # override serializer create func
    def create(self, validated_data):
        # flps
        print('\nin create block\n')
        # print('\n' + str(**validated_data) + '\n')
        # print('\n' + str(validated_data) + '\n')
        print('\npoppin items off of validated_data\n')
        flp_items_data = validated_data.pop('flp_items')
        print('\popped items off of validated_data\n')
        flp_order = Order.objects.create(**validated_data)

        for item_data in flp_items_data:
            OrderFlpItem.objects.create(order=flp_order, **item_data)
        
        return flp_order
    
# Order Flp Serializer
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
            "items",
            "stripe_token",
        )

    # override serializer create func
    def create(self, validated_data):
        # remove track data
        track_items_data = validated_data.pop('items')
        track_order = Order.objects.create(**validated_data)

        for item_data in track_items_data:
            OrderTrackItem.objects.create(order=track_order, **item_data)
        
        return track_order