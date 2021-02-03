# Generated by Django 3.1.6 on 2021-02-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210203_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'France'), ('sw', 'Swahili'), ('wf', 'Wolof'), ('ha', 'Hausa'), ('pe', 'Portuguese'), ('sp', 'Spanish')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('fr', 'France'), ('sw', 'Swahili'), ('wf', 'Wolof'), ('ha', 'Hausa'), ('pe', 'Portuguese'), ('sp', 'Spanish')], max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='superhost',
            field=models.BooleanField(default=False),
        ),
    ]
