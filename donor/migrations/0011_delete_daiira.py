# Generated by Django 4.2 on 2023-04-13 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0010_alter_daiira_wilaya_n_alter_donor_n_tel_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Daiira',
        ),
    ]