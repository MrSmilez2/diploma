# Generated by Django 3.0.5 on 2020-05-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers_app', '0003_auto_20200505_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='number_of_comments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='number_of_dislikes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='number_of_likes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='number_of_views',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='date_of_last_email',
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='location',
            field=models.CharField(max_length=20),
        ),
    ]
