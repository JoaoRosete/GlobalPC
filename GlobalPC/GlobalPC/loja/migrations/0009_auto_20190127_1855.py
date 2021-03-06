# Generated by Django 2.1.3 on 2019-01-27 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0008_userprofile_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='loja.Product'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='loja.UserProfile'),
        ),
    ]
