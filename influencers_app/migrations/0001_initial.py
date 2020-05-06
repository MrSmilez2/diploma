# Generated by Django 3.0.5 on 2020-05-05 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Influencer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_last_email', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('channels_url', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=20, unique=True)),
                ('subscribers', models.IntegerField()),
                ('email', models.CharField(max_length=50, unique=True)),
                ('progress', models.CharField(choices=[('RD', 'Review done'), ('AR', 'Awaiting review'), ('PS', 'Product sent'), ('CM', 'Communicating'), ('OD', 'Offer declined'), ('RJ', 'Rejection'), ('ES', 'Email inquiry sent'), ('OH', 'On hold')], default='ES', max_length=2)),
                ('review_notes', models.TextField()),
                ('number_of_folloups', models.IntegerField()),
                ('permission_for_ads', models.BooleanField()),
                ('notes', models.TextField()),
                ('website', models.CharField(max_length=45, unique=True)),
                ('responsible', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsible', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_publication', models.DateField()),
                ('number_of_views', models.IntegerField()),
                ('number_of_comments', models.IntegerField()),
                ('number_of_likes', models.IntegerField()),
                ('number_of_dislikes', models.IntegerField()),
                ('channel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='influencers_app.Influencer')),
            ],
        ),
    ]
