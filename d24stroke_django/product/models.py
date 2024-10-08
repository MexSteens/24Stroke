from distutils.command.upload import upload
from io import BytesIO
from unicodedata import category
# from unicodedata import category
from PIL import Image as PImage

from django.core.files import File
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class Address(models.Model):
#     country = models.CharField(max_length=255, default="Nederland", blank=True, null=True)
#     city = models.CharField(max_length=255, blank=True, null=True)
#     postal_code = models.CharField(max_length=7, blank=True, null=True)
#     street = models.CharField(max_length=255, blank=True, null=True)
#     house_number = models.CharField(max_length=255, blank=True, null=True)


# class User(AbstractUser):
#     first_name = models.CharField(max_length=255, blank=True, null=True)
#     last_name = models.CharField(max_length=255, blank=True, null=True)
#     phone_number = models.CharField(max_length=255, blank=True, null=True)
#     address = models.ForeignKey(Address, related_name="address", on_delete=models.CASCADE, blank=True, null=True)


class Category(models.Model):
    # parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'



class TechnicalDetails(models.Model):
    name = models.CharField(max_length=255, default="")
    article_number = models.CharField(max_length=255, default="")
    ean = models.IntegerField(default=0)
    brand = models.CharField(max_length=50, default="")
    moped = models.CharField(max_length=255, blank=True, null=True)

    class TuningLevel(models.TextChoices):
        Original = 'Original'
        Stage1 = 'Stage 1'
        Stage2 = 'Stage 2'
        Stage3 = 'Stage 3'
        Stage4 = 'Stage 4'

    tuning_level = models.CharField(choices=TuningLevel.choices, blank=True, null=True, max_length=50)
    material = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=40)
    cylinder_displacement = models.CharField(max_length=7, blank=True, null=True)
    cylinder_piston_pin = models.CharField(max_length=7, blank=True, null=True)
    cylinder_bore = models.CharField(max_length=7, blank=True, null=True)
    cylinder_stroke = models.CharField(max_length=40, blank=True, null=True)
    cylinder_conrod_length = models.CharField(max_length=40, blank=True, null=True)
    bougie_thread = models.CharField(max_length=40, blank=True, null=True)
    carburetor_type = models.CharField(max_length=10, blank=True, null=True)
    carburetor_diameter = models.CharField(max_length=7, blank=True, null=True)
    carburetor_airfilter_connection = models.CharField(max_length=7, blank=True, null=True)
    carburetor_manifold_connection = models.CharField(max_length=7, blank=True, null=True)
    carburetor_choke = models.CharField(max_length=50, blank=True, null=True)
    carburetor_ports = models.CharField(max_length=255, blank=True, null=True)
    variator_roller_size = models.CharField(max_length=50, blank=True, null=True)
    variator_roller_weight = models.CharField(max_length=200, blank=True, null=True)
    
    class VariatorRange(models.TextChoices):
        Standerd = 'Standard'
        Oversized = 'Oversized'

    variator_range = models.CharField(choices=VariatorRange.choices, blank=True, null=True, max_length=50)
    clutch_diameter = models.CharField(max_length=7, blank=True, null=True)
    transmission_type = models.CharField(max_length=25, blank=True, null=True)

    class IgnitionLightingSupply(models.TextChoices):
        Yes = 'With lighting power supply'
        No = 'Without lighting power supply'

    ignition_lighting_supply = models.CharField(choices=IgnitionLightingSupply.choices, blank=True, null=True, max_length=50)
    light_style = models.CharField(max_length=20, blank=True, null=True)
    light_voltage = models.CharField(max_length=40, blank=True, null=True)
    tire_width = models.CharField(max_length=50, blank=True, null=True)
    tire_height = models.CharField(max_length=50, blank=True, null=True)
    tire_rim_diameter = models.CharField(max_length=50, blank=True, null=True)
    tire_code = models.CharField(max_length=50, blank=True, null=True)
    tire_application = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class TechnicalDetailsDutch(models.Model):
    naam = models.CharField(max_length=255, default="")
    artikel_nummer = models.CharField(max_length=255, default="")
    ean = models.IntegerField(default=0)
    merk = models.CharField(max_length=50, default="")
    brommer = models.CharField(max_length=255, blank=True, null=True)

    class TuningLevel(models.TextChoices):
        Original = 'Original'
        Stage1 = 'Stage 1'
        Stage2 = 'Stage 2'
        Stage3 = 'Stage 3'
        Stage4 = 'Stage 4'

    tuning_level = models.CharField(choices=TuningLevel.choices, blank=True, null=True, max_length=50)
    materiaal = models.CharField(max_length=30, blank=True, null=True)
    kleur = models.CharField(max_length=40)
    cilinderinhoud = models.CharField(max_length=7, blank=True, null=True)
    pistonpen = models.CharField(max_length=7, blank=True, null=True)
    boring = models.CharField(max_length=7, blank=True, null=True)
    krukas_slag = models.CharField(max_length=40, blank=True, null=True)
    drijfstang_lengte = models.CharField(max_length=40, blank=True, null=True)
    draad_bougie = models.CharField(max_length=40, blank=True, null=True)
    type_carburateur = models.CharField(max_length=10, blank=True, null=True)
    diameter_carburateur = models.CharField(max_length=7, blank=True, null=True)
    luchtfilter_connectie = models.CharField(max_length=7, blank=True, null=True)
    spruitstuk_connectie = models.CharField(max_length=7, blank=True, null=True)
    choke_carburateur = models.CharField(max_length=50, blank=True, null=True)
    poorten_carburateur = models.CharField(max_length=255, blank=True, null=True)
    grootte_rollen_variateur = models.CharField(max_length=50, blank=True, null=True)
    gewicht_rollen_variateur = models.CharField(max_length=200, blank=True, null=True)
    
    class VariatorRange(models.TextChoices):
        Standerd = 'Standaard'
        Oversized = 'Oversized'

    lengte_variateur = models.CharField(choices=VariatorRange.choices, blank=True, null=True, max_length=50)
    diameter_koppeling = models.CharField(max_length=7, blank=True, null=True)
    type_transmissie = models.CharField(max_length=25, blank=True, null=True)

    class IgnitionLightingSupply(models.TextChoices):
        Yes = 'Met lichtspoel'
        No = 'zonder lichtspoel'

    lichtspoel_ontsteking = models.CharField(choices=IgnitionLightingSupply.choices, blank=True, null=True, max_length=50)
    style_lamp = models.CharField(max_length=20, blank=True, null=True)
    voltage_lamp = models.CharField(max_length=40, blank=True, null=True)
    breedte_band = models.CharField(max_length=50, blank=True, null=True)
    hoogte_band = models.CharField(max_length=50, blank=True, null=True)
    velg_diameter_band = models.CharField(max_length=50, blank=True, null=True)
    code_band = models.CharField(max_length=50, blank=True, null=True)
    toepassing_band = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.naam


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    technical_details = models.ForeignKey(TechnicalDetails, related_name="technical_details", on_delete=models.CASCADE, blank=True, null=True)
    technical_details_dutch = models.ForeignKey(TechnicalDetailsDutch, related_name="technical_details_dutch", on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # images = models.ManyToManyField(Image, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = PImage.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class Image(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.product.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

class HighlightedProduct(models.Model):
    product = models.ForeignKey(Product, related_name="highlighted_products", on_delete=models.CASCADE)
    discounted_deal = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    highlight_until = models.DateTimeField()

    def __str__(self):
        return '%s' % self.product.name


class Subscriber(models.Model):
    email = models.EmailField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.email
    