# Generated by Django 3.0.2 on 2020-01-13 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0019_remove_animal_climate'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='climate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='animals.Climate'),
        ),
    ]
