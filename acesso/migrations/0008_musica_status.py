# Generated by Django 4.0.5 on 2023-05-02 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acesso', '0007_musica'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='status',
            field=models.TextField(default='', max_length=10),
        ),
    ]