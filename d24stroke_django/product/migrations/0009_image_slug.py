# Generated by Django 4.0.3 on 2022-06-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_image_category_remove_image_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255)),
        ),
    ]
