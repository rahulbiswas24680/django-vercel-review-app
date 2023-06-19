from django.db import models
from primary.models import *
import choices
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import *


class Review(models.Model):
     """
     Base review class for any product
     """

     category = models.ForeignKey(Category, on_delete=models.PROTECT)
     brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True, blank=True)
     model = models.ForeignKey(Model, on_delete=models.PROTECT, null=True, blank=True)
     
     ques_cluster = models.ForeignKey(QuestionCluster, on_delete=models.PROTECT, null=True, blank=True)

     rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
     image_urls = models.JSONField(blank=True, null=True)
     video_urls = models.JSONField(blank=True, null=True)

     reviewed_by = models.ForeignKey(PlatformAndUserConnector, on_delete=models.PROTECT, null=True, blank=True)
     review_of_user = models.ForeignKey(ProductUser, on_delete=models.PROTECT)

     price_of_review = models.DecimalField(max_digits=19, decimal_places=10)
     payment_of_connector = models.CharField(choices=choices.payment_status, max_length=30, null=True, blank=True)
     payment_of_product_user = models.CharField(choices=choices.payment_status, max_length=30, null=True, blank=True)

     is_active = models.BooleanField(default=True)
     created_at = models.DateTimeField(auto_now_add=True)
     modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
     created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
     modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='review_modified_by')



class OrderOfReview(models.Model):
     """
     Buyers ordered reviews class 
     """
     review_ids = models.JSONField()
     bought_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, related_name='ordered_review')
     gst = models.DecimalField(max_digits=19, decimal_places=10)
     is_active = models.BooleanField(default=True)
     created_at = models.DateTimeField(auto_now_add=True)
     modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
     created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
     modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='order_of_review_modified_by')



class PaymentForReview(models.Model):
     """
     Payment class for users who are contributed in reviews
     """
     payment_type = models.CharField(choices=choices.payment_type, max_length=30)
     payment_method = models.CharField(choices=choices.payment_method, max_length=30)
     payment_date = models.DateTimeField()
     payment_price = models.DecimalField(max_digits=19, decimal_places=10)
     payment_due_price = models.DecimalField(max_digits=19, decimal_places=10)
     payment_to = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='user_payment')
     payment_status = models.CharField(choices=choices.payment_status, max_length=30)

     is_active = models.BooleanField(default=True)
     created_at = models.DateTimeField(auto_now_add=True)
     modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
     created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
     modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='payment_for_review_modified_by')