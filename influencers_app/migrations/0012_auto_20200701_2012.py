# Generated by Django 3.0.5 on 2020-07-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers_app', '0011_auto_20200629_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencersinformation',
            name='date_of_last_email',
            field=models.DateField(auto_created=True, blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='influencersinformation',
            name='location',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='influencersinformation',
            name='notes',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='influencersinformation',
            name='number_of_followups',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='influencersinformation',
            name='permission_for_ads',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='influencersinformation',
            name='review_notes',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='influencersinformation',
            name='subscribers',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='influencersinformation',
            name='website',
            field=models.CharField(default=None, max_length=45, null=True, unique=True),
        ),
    ]
