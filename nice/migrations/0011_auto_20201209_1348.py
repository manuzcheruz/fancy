# Generated by Django 2.2.6 on 2020-12-09 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nice', '0010_auto_20201209_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='nice.Category'),
            preserve_default=False,
        ),
    ]
