from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import *
import choices

##################################
# Product Related Tables         #
##################################

class Category(models.Model):
    name =  models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
    modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='category_modified_by')


class Brand(models.Model):
    name =  models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
    modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='brand_modified_by')

    def __str__(self) -> str:
        return str(self.name) + '-' + str(self.category.name)
    

class Variant(models.Model):
    name =  models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
    modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='variant_modified_by')


class Model(models.Model):
    name =  models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
    modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='model_modified_by')

    def __str__(self) -> str:
        return str(self.name) + '-' + str(self.brand.name)
    


class Question(models.Model):
    ques_title = models.CharField(max_length=200)
    ques_importance = models.IntegerField(blank=True, null=True)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
    modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='ques_modified_by')


class QuestionCluster(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(choices=choices.brand_choice, max_length=30, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
    modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='ques_cluster_modified_by')




##################################
# UserProfile Related Tables         #
##################################

class PlatformAndUserConnector(models.Model):
    connector_name = models.CharField(max_length=200)
    gstin = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email_id = models.CharField(max_length=25, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    bank_account_number = models.CharField(max_length=40, blank=True, null=True)
    ifsc_code = models.CharField(max_length=10, blank=True, null=True)
    account_holder_name = models.CharField(max_length=50, blank=True, null=True)
    linked_mobile_number = models.CharField(max_length=15, blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    performance_status = models.CharField(choices=choices.performance_choices, max_length=20, null=True, blank=True)
    total_created_entry = models.PositiveIntegerField(blank=True, null=True)
    total_earned_amount = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    staff_account = models.PositiveIntegerField(blank=True, null=True)

    user = models.ForeignKey(UsersData, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
    modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='platform_and_user_connector_modified_by')


class ProductUser(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email_id = models.CharField(max_length=25, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
    modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='product_user_modified_by')


class ReviewBuyer(models.Model):
    company_name = models.CharField(max_length=200, blank=True, null=True)
    brand_name = models.ForeignKey(Brand, on_delete=models.PROTECT, blank=True, null=True)
    gstin = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email_id = models.CharField(max_length=25, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    buyer_brand_rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    total_created_entry = models.PositiveIntegerField(blank=True, null=True)
    total_spent_amount = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)

    user = models.ForeignKey(UsersData, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True)
    modified_by = models.ForeignKey(CredentialsData, on_delete=models.PROTECT, null=True, blank=True, related_name='review_buyer_modified_by')