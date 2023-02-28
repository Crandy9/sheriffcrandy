# import lctec custom user
from django.contrib.auth import get_user_model
from django.db import models

# connect orders to users
User = get_user_model()

# import flps/tracks models
from flps_app.models import Flp
from tracks_app.models import Track

# order model with customer's billing info
class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    statePref = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    order_created=models.DateTimeField(auto_now=True)
    usd_paid_amount= models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    jpy_paid_amount = models.IntegerField(default=0, null=True, blank=True)
    stripe_token = models.CharField(max_length=100)

    class Meta: 
        ordering = ['-order_created',]

    def __str__(self):
        return self.name
    
# Order Item, either flp or track
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    # flp items
    flp = models.ForeignKey(Flp, related_name='items', on_delete=models.CASCADE)
    usd_flp_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    jpy_flp_price = models.IntegerField(default=0, null=True, blank=True)
    flp_quantity = models.IntegerField(default = 0)
    # track items
    track = models.ForeignKey(Track, related_name='items', on_delete=models.CASCADE)
    usd_track_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    jpy_track_price = models.IntegerField(default=0, null=True, blank=True)
    track_quantity = models.IntegerField(default = 0)

    def __str__(self):
        # string representation of the id
        return '%s' % self.id