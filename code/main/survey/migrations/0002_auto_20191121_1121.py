# Generated by Django 2.2.6 on 2019-11-21 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='fruit',
            field=models.CharField(choices=[('a', 'แอปเปิ้ล'), ('b', 'มะละกอ'), ('c', 'กล้วย'), ('d', 'ส้ม')], max_length=1),
        ),
        migrations.AlterField(
            model_name='survey',
            name='gender',
            field=models.CharField(choices=[('F', 'หญิง'), ('M', 'ชาย')], max_length=1),
        ),
    ]
