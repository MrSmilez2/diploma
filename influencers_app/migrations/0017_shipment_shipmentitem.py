# Generated by Django 3.0.5 on 2020-07-06 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('influencers_app', '0016_auto_20200705_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipmentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(related_name='products', to='influencers_app.ArtzProductUS')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_status', models.CharField(choices=[('Need to be shipped', 'Need to be shipped'), ('Shipped', 'Shipped')], default='Need to be shipped', max_length=18)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('order_number', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('channel_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='influencers_app.Influencer')),
            ],
        ),
    ]
