# Generated by Django 5.0.6 on 2024-05-09 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0004_alter_filme_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='thumb',
            field=models.ImageField(upload_to='thumb_filmes/'),
        ),
    ]
