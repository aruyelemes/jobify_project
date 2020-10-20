# Generated by Django 3.0.3 on 2020-05-03 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quesiton', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=100)),
                ('var1', models.CharField(max_length=100)),
                ('var2', models.CharField(max_length=100)),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('plan', models.ManyToManyField(to='items.PlanItem')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('quiz', models.ManyToManyField(to='items.Quiz')),
                ('stack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
