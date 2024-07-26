# Generated by Django 5.0.7 on 2024-07-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='uploads/default.png', upload_to='uploads/')),
                ('name', models.CharField(default='Asic', max_length=100)),
                ('price', models.PositiveIntegerField(default=0, null=True)),
                ('link', models.URLField(default='https://shop.bitmain.com')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]