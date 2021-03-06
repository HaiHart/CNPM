# Generated by Django 3.2.9 on 2021-11-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('qtity', models.IntegerField(default=0)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('src', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoodOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('food', models.ManyToManyField(blank=True, to='foodStore.Food')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='side',
            field=models.ManyToManyField(blank=True, to='foodStore.Side'),
        ),
        migrations.AddField(
            model_name='food',
            name='type',
            field=models.ManyToManyField(blank=True, to='foodStore.Type'),
        ),
    ]
