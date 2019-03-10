# Generated by Django 2.1.7 on 2019-03-09 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190309_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car', to='user.Course', verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='order',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='user.Course', verbose_name='课程'),
        ),
    ]
