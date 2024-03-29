# Generated by Django 2.1.7 on 2020-06-27 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=4, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=4, max_digits=9)),
                ('total_price', models.DecimalField(decimal_places=4, max_digits=20)),
                ('ImportingUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pro_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.Category_list')),
                ('pro_vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.AllVendor')),
            ],
        ),
    ]
