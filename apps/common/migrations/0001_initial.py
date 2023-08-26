# Generated by Django 4.2.4 on 2023-08-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=600)),
                ('project_name', models.CharField(max_length=600)),
                ('phone_number', models.CharField(max_length=600)),
                ('address', models.TextField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('moderation', 'Moderation'), ('cancelled', 'Cancelled')], max_length=300)),
            ],
        ),
    ]