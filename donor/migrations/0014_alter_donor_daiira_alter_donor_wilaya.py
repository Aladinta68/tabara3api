# Generated by Django 4.2 on 2023-04-13 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0013_alter_daiira_wilaya_n'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='daiira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.daiira'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.wilaya'),
        ),
    ]
