# Generated by Django 3.1.4 on 2020-12-14 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scooter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='service date')),
                ('oil', models.CharField(choices=[('R', 'Regular'), ('B', 'Blend'), ('S', 'Synthetic')], default='R', max_length=1)),
                ('scooter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.scooter')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]