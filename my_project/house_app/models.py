from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField()
    Role_Choices = (
        ('seller', 'seller'),
        ('buyer', 'buyer')
    )
    role = models.CharField(choices=Role_Choices, max_length=32, default='buyer')
    created_date = models.DateTimeField(auto_now_add=True)

class Region(models.Model):
    region_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.region_name

class City(models.Model):
    city_name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

class District(models.Model):
    district_name = models.CharField(max_length=64, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.district_name

class Property(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    PROPERTY_TYPE = (
        ('Квартира', 'Квартира'),
        ('Дом', 'Дом'),
        ('Коммерческая недвижимость', 'Коммерческая недвижимость'),
        ('Комната', 'Комната'),
        ('Участок', 'Участок'),
        ('Дача', 'Дача')
    )
    property_type = models.CharField(choices=PROPERTY_TYPE, max_length=64)
    Transaction_Choices = (
        ('снять', 'снять'),
        ('купить', 'купить')
    )
    type_transaction = models.CharField(choices=Transaction_Choices, max_length=32)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=4, decimal_places=1)
    price = models.PositiveSmallIntegerField()
    Room_Choices = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('свободная планировка', 'свободная планировка')
    )
    room = models.CharField(choices=Room_Choices,max_length=56)
    floor = models.PositiveSmallIntegerField()
    total_floor = models.PositiveSmallIntegerField()
    Condition_Choices = (
        ('под самоотделку', 'под самоотделку'),
        ('евроремонт', 'евроремонт'),
        ('хорошее', 'хорошее'),
        ('среднее', 'среднее'),
        ('не достроено', 'не достроено')
    )
    condition = models.CharField(choices=Condition_Choices, max_length=32)
    document = models.BooleanField()
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_avg_rating(self):
        ratings = self.property_review.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 2 )
        return 0

    def get_count_review(self):
        self.property_review.count()


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_images')
    property_image = models.ImageField(upload_to='property_photo/')

class Review(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='review_seller')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_review')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)],null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)