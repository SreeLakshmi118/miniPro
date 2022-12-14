# Generated by Django 4.1 on 2022-10-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=250, unique=True)),
                ('file', models.FileField(upload_to='music')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='b_name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
