# Generated by Django 5.0.2 on 2024-02-20 00:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('color', models.CharField(max_length=32)),
                ('length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('curl_pattern', models.CharField(choices=[('curly', 'Curly'), ('straight', 'Straight')], max_length=16)),
                ('density', models.IntegerField()),
                ('hair_origin', models.CharField(choices=[('brazilian', 'Brazilian'), ('peruvian', 'Peruvian')], max_length=16)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]