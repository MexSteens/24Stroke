# Generated by Django 4.0.3 on 2023-01-23 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('article_number', models.CharField(default='', max_length=255)),
                ('ean', models.IntegerField(default=0)),
                ('brand', models.CharField(default='', max_length=50)),
                ('moped', models.CharField(blank=True, max_length=255, null=True)),
                ('tuning_level', models.CharField(blank=True, choices=[('Original', 'Original'), ('Stage 1', 'Stage1'), ('Stage 2', 'Stage2'), ('Stage 3', 'Stage3'), ('Stage 4', 'Stage4')], max_length=50, null=True)),
                ('material', models.CharField(blank=True, max_length=30, null=True)),
                ('colour', models.CharField(max_length=40)),
                ('cylinder_displacement', models.CharField(blank=True, max_length=7, null=True)),
                ('cylinder_piston_pin', models.CharField(blank=True, max_length=7, null=True)),
                ('cylinder_bore', models.CharField(blank=True, max_length=7, null=True)),
                ('cylinder_stroke', models.CharField(blank=True, max_length=40, null=True)),
                ('cylinder_conrod_length', models.CharField(blank=True, max_length=40, null=True)),
                ('bougie_thread', models.CharField(blank=True, max_length=40, null=True)),
                ('carburetor_type', models.CharField(blank=True, max_length=10, null=True)),
                ('carburetor_diameter', models.CharField(blank=True, max_length=7, null=True)),
                ('carburetor_airfilter_connection', models.CharField(blank=True, max_length=7, null=True)),
                ('carburetor_manifold_connection', models.CharField(blank=True, max_length=7, null=True)),
                ('carburetor_choke', models.CharField(blank=True, max_length=50, null=True)),
                ('carburetor_ports', models.CharField(blank=True, max_length=255, null=True)),
                ('variator_roller_size', models.CharField(blank=True, max_length=50, null=True)),
                ('variator_roller_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('variator_range', models.CharField(blank=True, choices=[('Standerd', 'Standerd'), ('Oversized', 'Oversized')], max_length=50, null=True)),
                ('clutch_diameter', models.CharField(blank=True, max_length=7, null=True)),
                ('transmission_type', models.CharField(blank=True, max_length=25, null=True)),
                ('ignition_lighting_supply', models.CharField(blank=True, choices=[('With lighting power supply', 'Yes'), ('Without lighting power supply', 'No')], max_length=50, null=True)),
                ('light_style', models.CharField(blank=True, max_length=20, null=True)),
                ('light_voltage', models.CharField(blank=True, max_length=40, null=True)),
                ('tire_width', models.CharField(blank=True, max_length=50, null=True)),
                ('tire_height', models.CharField(blank=True, max_length=50, null=True)),
                ('tire_rim_diameter', models.CharField(blank=True, max_length=50, null=True)),
                ('tire_code', models.CharField(blank=True, max_length=50, null=True)),
                ('tire_application', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
                ('technical_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='technical_details', to='product.technicaldetails')),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('default', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='HighlightedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discounted_deal', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('highlight_until', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='highlighted_products', to='product.product')),
            ],
        ),
    ]
