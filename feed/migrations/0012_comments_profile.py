# Generated by Django 2.1 on 2023-01-28 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200815_0840'),
        ('feed', '0011_auto_20230116_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
