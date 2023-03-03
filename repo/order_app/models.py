# import lctec custom user
from django.contrib.auth import get_user_model
from django.db import models

# import flps/tracks models
from flps_app.models import Flp
from tracks_app.models import Track


# connect orders to users
User = get_user_model()

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
    date_order_created = models.DateTimeField(auto_now=True)
    usd_paid_amount= models.DecimalField(default=0, max_digits=8, decimal_places=2, blank=True, null=True)
    jpy_paid_amount = models.IntegerField(default=0, null=True, blank=True)
    stripe_token = models.CharField(max_length=100, null=True, blank=True)

    class Meta: 
        verbose_name = "Stripe Order (for FLPs and tracks)"
        verbose_name_plural = "Stripe Orders (for FLPs and tracks)"
        ordering = ['-date_order_created',]

    def __str__(self):

        dtformat = self.date_order_created.strftime("%Y/%m/%d, %H:%M:%S")
        # string representation of object using name
        return "Order ID: " + '%s' % self.id + f'\nUser: {self.user.username}\nOrder Date: ' + str(dtformat)
    
# Order Item for flp
class OrderFlpItem(models.Model):
    order = models.ForeignKey(Order, related_name='flp_items', on_delete=models.CASCADE)
    flp = models.ForeignKey(Flp, related_name='flp_items', on_delete=models.CASCADE)
    date_order_created = models.DateTimeField(auto_now=True)

    # for readability in admin site
    class Meta:
        verbose_name = "FLP Orders"
        verbose_name_plural = "FLP Orders"

    def __str__(self):
        dtformat = self.date_order_created.strftime("%Y/%m/%d, %H:%M:%S")
        # admin page title display
        return "Order ID: " + '%s' % self.order.id + ' Flp: ' + str(self.flp.flp_name) + '\nOrder Date: ' + str(dtformat)
    
# Same model for tracks
class OrderTrackItem(models.Model):
    order = models.ForeignKey(Order, related_name='track_items', on_delete=models.CASCADE)
    track = models.ForeignKey(Track, related_name='track_items', on_delete=models.CASCADE)
    date_order_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Track Orders"
        verbose_name_plural = "Track Orders"

    def __str__(self):
        dtformat = self.date_order_created.strftime("%Y/%m/%d, %H:%M:%S")
        return "Order ID: " + '%s' % self.order.id + ' Track: ' + str(self.track.title) + '\nOrder Date: ' + str(dtformat)