from django.db import models


class Category(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=40)
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subcategories',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title} - {self.parent_category}'
    
    class Meta:
        db_table = 'category'


class OfferPicture(models.Model):
    offer = models.ForeignKey(
        'Offer',
        related_name='pictures',
        on_delete=models.CASCADE
    )
    picture_url = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.offer.name} - {self.picture_url}'
    
    class Meta:
        db_table = 'offer_picture'


class Product(models.Model):
    name = models.CharField(max_length=120)
    percent = models.IntegerField()
    category = models.ManyToManyField(
        Category,
        related_name='products',
    )
    vat = models.IntegerField()
    model = models.CharField(max_length=120, unique=True)
    vendor_code = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField()
    price_begin = models.FloatField()

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table = 'product'


class Offer(models.Model):
    # id = models.BigIntegerField(primary_key=True, unique=True)
    barcode = models.CharField(max_length=120, primary_key=True, unique=True)
    name = models.CharField(max_length=120)
    available = models.BooleanField()
    product = models.ForeignKey(
        Product,
        related_name='offers',
        on_delete=models.CASCADE
    )
    params = models.JSONField()

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table = 'offer'

    # id = models.BigIntegerField(primary_key=True, unique=True)
    # name = models.CharField(max_length=120)
    # price = models.FloatField()
    # price_begin = models.FloatField()
    # percent = models.IntegerField()
    # category = models.ManyToManyField(
    #     Category,
    #     related_name='offers',
    # )
    # vat = models.IntegerField()
    # model = models.CharField(max_length=120)
    # vendor_code = models.CharField(max_length=120)
    # description = models.TextField()
    # barcode = models.CharField(max_length=120)
    # params = models.JSONField()