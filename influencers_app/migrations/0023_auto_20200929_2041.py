# Generated by Django 3.0.5 on 2020-09-29 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('influencers_app', '0022_auto_20200929_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='type_of_social_media1',
            new_name='type_of_social_media',
        ),
    ]