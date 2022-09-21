# Generated by Django 4.1 on 2022-09-21 00:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_alter_entrada_fecha_alter_entrada_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='likes',
        ),
        migrations.AddField(
            model_name='entrada',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
