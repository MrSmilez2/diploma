# Generated by Django 3.0.5 on 2020-07-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("influencers_app", "0013_auto_20200701_2013"),
    ]

    operations = [
        migrations.AlterField(
            model_name="influencersinformation",
            name="notes",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="influencersinformation",
            name="number_of_followups",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="influencersinformation",
            name="permission_for_ads",
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="influencersinformation",
            name="review_notes",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="influencersinformation",
            name="subscribers",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="influencersinformation",
            name="website",
            field=models.CharField(
                blank=True, default=None, max_length=45, null=True, unique=True
            ),
        ),
    ]
