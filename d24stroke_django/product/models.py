from distutils.command.upload import upload
from io import BytesIO
from unicodedata import category
# from unicodedata import category
from PIL import Image as PImage

from django.core.files import File
from django.db import models

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True )
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
        Standerd = 'Standerd'
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


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    technical_details = models.ForeignKey(TechnicalDetails, related_name="technical_details", on_delete=models.CASCADE, blank=True, null=True)
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

class Subscriber(models.Model):
    email = models.EmailField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.email
    