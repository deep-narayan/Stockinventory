# Generated by Django 2.1.7 on 2020-06-28 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0002_importproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.DecimalField(decimal_places=4, max_digits=9)),
                ('cost_price', models.DecimalField(decimal_places=4, max_digits=9)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('ImportingUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pro_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.Category_list')),
            ],
        ),
    ]
