# Generated by Django 3.2.4 on 2021-06-10 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teste',
            old_name='idade',
            new_name='idade_pessoa',
        ),
    ]