# Generated by Django 5.1.6 on 2025-03-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_service_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.CharField(blank=True, max_length=255, null=True)),
                ('rating_count', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('user_job_title', models.CharField(max_length=50)),
            ],
        ),
    ]
