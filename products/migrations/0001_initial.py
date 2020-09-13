# Generated by Django 2.2.15 on 2020-09-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('pub_date', models.DateField()),
                ('votes_total', models.IntegerField(default=1)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/')),
                ('icon', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]