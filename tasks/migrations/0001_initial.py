# Generated by Django 4.2.5 on 2023-09-25 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_estudiante', models.CharField(max_length=10, unique=True)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
    ]
