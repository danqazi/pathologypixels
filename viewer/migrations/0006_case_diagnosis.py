# Generated by Django 3.0.7 on 2020-06-06 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_auto_20200605_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='diagnosis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='viewer.Diagnosis'),
        ),
    ]