# Generated by Django 3.0.5 on 2020-07-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("influencers_app", "0015_auto_20200701_2107"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArtzProductUS",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sku", models.IntegerField(unique=True)),
                ("product_name", models.CharField(max_length=100)),
                ("product_price", models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name="influencersinformation",
            name="progress",
            field=models.CharField(
                choices=[
                    ("1RD", "Review done"),
                    ("2AR", "Awaiting review"),
                    ("3PS", "Product sent"),
                    ("4CM", "Communicating"),
                    ("5OD", "Offer declined"),
                    ("6RJ", "Rejection"),
                    ("7ES", "Email inquiry sent"),
                    ("8OH", "On hold"),
                    ("9DV", "Send your first message"),
                ],
                default="9DV",
                max_length=3,
            ),
        ),
    ]
