# Generated by Django 3.2.2 on 2022-08-09 13:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedCollection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=500)),
                ('buy_text', models.CharField(max_length=500)),
                ('image', models.FileField(blank=True, upload_to='back-end-image/FeaturedCollection/')),
            ],
            options={
                'db_table': 'featured-collection',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HeroImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=500)),
                ('buy_text', models.CharField(max_length=500)),
                ('image', models.FileField(blank=True, upload_to='back-end-image/HeroImage/')),
            ],
            options={
                'db_table': 'hero-image',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InterestCheck',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=1000)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('image', models.FileField(blank=True, upload_to='back-end-image/ProductImage/')),
            ],
            options={
                'db_table': 'interest-check',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('specs', models.CharField(max_length=500, verbose_name='Specs')),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'product',
                'managed': True,
                'unique_together': {('category', 'title')},
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('image', models.FileField(blank=True, upload_to='back-end-image/ProductImage/')),
                ('ranking', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_photos', to='mechaland.product')),
            ],
            options={
                'db_table': 'product-image',
                'ordering': ('ranking',),
                'managed': True,
            },
        ),
    ]
