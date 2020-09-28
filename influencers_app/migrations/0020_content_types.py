# Generated by Django 3.0.5 on 2020-09-27 08:47

from django.db import migrations
import enumchoicefield.fields
import influencers_app.enums


class Migration(migrations.Migration):

    dependencies = [
        ('influencers_app', '0019_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='type_of_social_media',
            field=enumchoicefield.fields.EnumChoiceField(default=None, enum_class=influencers_app.enums.ContentType, max_length=14),
        ),
    ]